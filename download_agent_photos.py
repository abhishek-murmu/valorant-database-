import json
import os
import re
import urllib.request


BASE_DIR = os.path.dirname(__file__)
PHOTO_DIR = os.path.join(BASE_DIR, "agents", "photos")
API_URL = "https://valorant-api.com/v1/agents?isPlayableCharacter=true"
USER_AGENT = "Mozilla/5.0"

DB_AGENT_ALIASES = {
    "KAY/O": "KAY/O",
}


def slugify_name(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", str(name).strip().lower()).strip("_")


def fetch_json(url: str) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def fetch_bytes(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def load_db_agent_names() -> list[str]:
    try:
        import mysql.connector
        from dotenv import load_dotenv
    except ImportError as exc:
        raise RuntimeError("Missing required packages to query the local database.") from exc

    load_dotenv(os.path.join(BASE_DIR, ".env"))
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT", "3306")),
    )
    cur = conn.cursor()
    cur.execute("SELECT agent_name FROM agents ORDER BY agent_name")
    names = [row[0] for row in cur.fetchall()]
    cur.close()
    conn.close()
    return names


def build_api_lookup() -> dict[str, dict]:
    payload = fetch_json(API_URL)
    lookup = {}
    for agent in payload.get("data", []):
        name = agent.get("displayName")
        if name:
            lookup[slugify_name(name)] = agent
    return lookup


def resolve_agent_record(agent_name: str, lookup: dict[str, dict]) -> dict | None:
    preferred_name = DB_AGENT_ALIASES.get(agent_name, agent_name)
    return lookup.get(slugify_name(preferred_name))


def choose_image_url(agent_record: dict) -> str | None:
    return (
        agent_record.get("displayIcon")
        or agent_record.get("bustPortrait")
        or agent_record.get("fullPortraitV2")
        or agent_record.get("fullPortrait")
    )


def build_output_path(agent_name: str) -> str:
    return os.path.join(PHOTO_DIR, f"{slugify_name(agent_name)}.png")


def main():
    os.makedirs(PHOTO_DIR, exist_ok=True)
    agent_names = load_db_agent_names()
    api_lookup = build_api_lookup()

    downloaded = 0
    missing = []

    for agent_name in agent_names:
        agent_record = resolve_agent_record(agent_name, api_lookup)
        if not agent_record:
            missing.append(agent_name)
            print(f"Missing API record for {agent_name}")
            continue

        image_url = choose_image_url(agent_record)
        if not image_url:
            missing.append(agent_name)
            print(f"Missing image for {agent_name}")
            continue

        image_bytes = fetch_bytes(image_url)
        output_path = build_output_path(agent_name)
        with open(output_path, "wb") as image_file:
            image_file.write(image_bytes)
        downloaded += 1
        print(f"Saved {agent_name} -> {output_path}")

    print(f"\nDownloaded {downloaded} agent photos.")
    if missing:
        print("Missing agents:")
        for agent_name in missing:
            print(f"- {agent_name}")


if __name__ == "__main__":
    main()
