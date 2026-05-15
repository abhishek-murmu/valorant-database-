import math

import mysql.connector
import pandas as pd
import streamlit as st

import os
import re

try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv(dotenv_path=".env"):
        if not os.path.exists(dotenv_path):
            return
        with open(dotenv_path, encoding="utf-8") as env_file:
            for raw_line in env_file:
                line = raw_line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, value = line.split("=", 1)
                os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
    "port": int(os.getenv("DB_PORT", "3306")),
}

MENU_ITEMS = [
    "Overview",
    "Teams",
    "Players",
    "Agents",
    "Maps",
    "Team Players",
    "Advance Query",
]

MISSING_TABLE_SQL = {
    "events": """
CREATE TABLE events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    event_name VARCHAR(255) NOT NULL UNIQUE,
    event_prize VARCHAR(100) NOT NULL,
    event_location VARCHAR(150) NOT NULL,
    event_dates VARCHAR(100) NOT NULL
);
""".strip(),
    "matches": """
CREATE TABLE matches (
    match_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT NOT NULL,
    event_stage VARCHAR(100) NOT NULL,
    match_series VARCHAR(100) NOT NULL,
    match_date DATE NOT NULL,
    match_time TIME NOT NULL,
    map_name VARCHAR(50),
    team1_id INT,
    team1_name VARCHAR(100) NOT NULL,
    team1_score INT NOT NULL,
    team2_id INT,
    team2_name VARCHAR(100) NOT NULL,
    team2_score INT NOT NULL,
    winner_team_id INT,
    winner_team_name VARCHAR(100) NOT NULL,
    winning_score VARCHAR(20) NOT NULL,
    status VARCHAR(50) NOT NULL,
    FOREIGN KEY (event_id) REFERENCES events(event_id),
    FOREIGN KEY (team1_id) REFERENCES teams(team_id),
    FOREIGN KEY (team2_id) REFERENCES teams(team_id),
    FOREIGN KEY (winner_team_id) REFERENCES teams(team_id)
);
""".strip(),
    "maps": """
CREATE TABLE maps (
    map_id INT AUTO_INCREMENT PRIMARY KEY,
    map_name VARCHAR(50) NOT NULL UNIQUE
);
""".strip(),
    "match_maps": """
CREATE TABLE match_maps (
    match_map_id INT AUTO_INCREMENT PRIMARY KEY,
    match_id INT NOT NULL,
    map_number INT NOT NULL,
    map_id INT,
    map_name VARCHAR(50) NOT NULL,
    team1_score INT,
    team2_score INT,
    winner_team_id INT,
    winner_team_name VARCHAR(100),
    UNIQUE KEY uniq_match_map (match_id, map_number),
    FOREIGN KEY (match_id) REFERENCES matches(match_id),
    FOREIGN KEY (map_id) REFERENCES maps(map_id),
    FOREIGN KEY (winner_team_id) REFERENCES teams(team_id)
);
""".strip(),
    "player_match_stats": """
CREATE TABLE player_match_stats (
    player_stat_id INT AUTO_INCREMENT PRIMARY KEY,
    match_id INT NOT NULL,
    player_id INT NOT NULL,
    kills INT DEFAULT 0,
    deaths INT DEFAULT 0,
    assists INT DEFAULT 0,
    acs DECIMAL(6,2) DEFAULT 0,
    FOREIGN KEY (match_id) REFERENCES matches(match_id),
    FOREIGN KEY (player_id) REFERENCES players(player_id)
);
""".strip(),
    "team_match_stats": """
CREATE TABLE team_match_stats (
    team_stat_id INT AUTO_INCREMENT PRIMARY KEY,
    match_id INT NOT NULL,
    team_id INT NOT NULL,
    rounds_won INT DEFAULT 0,
    rounds_lost INT DEFAULT 0,
    first_bloods INT DEFAULT 0,
    spike_plants INT DEFAULT 0,
    FOREIGN KEY (match_id) REFERENCES matches(match_id),
    FOREIGN KEY (team_id) REFERENCES teams(team_id)
);
""".strip(),
}

AGENT_IMAGE_DIR = os.path.join(os.path.dirname(__file__), "agents", "photos")
IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".webp")
AGENT_ORIGINS = {
    "Astra": "Ghana",
    "Breach": "Sweden",
    "Brimstone": "United States",
    "Chamber": "France",
    "Clove": "Scotland",
    "Cypher": "Morocco",
    "Deadlock": "Norway",
    "Fade": "Turkey",
    "Gekko": "United States",
    "Harbor": "India",
    "Iso": "China",
    "Jett": "South Korea",
    "KAY/O": "Unknown",
    "Killjoy": "Germany",
    "Miks": "Unknown",
    "Neon": "Philippines",
    "Omen": "Unknown",
    "Phoenix": "United Kingdom",
    "Raze": "Brazil",
    "Reyna": "Mexico",
    "Sage": "China",
    "Skye": "Australia",
    "Sova": "Russia",
    "Tejo": "Colombia",
    "Veto": "Unknown",
    "Viper": "United States",
    "Vyse": "Unknown",
    "Waylay": "Thailand",
    "Yoru": "Japan",
}
AGENT_NAME_THEMES = {
    "Astra": ("#6d28d9", "#f3e8ff", "#4c1d95"),
    "Breach": ("#b45309", "#ffedd5", "#7c2d12"),
    "Brimstone": ("#991b1b", "#fee2e2", "#7f1d1d"),
    "Chamber": ("#a16207", "#fef3c7", "#713f12"),
    "Clove": ("#7c3aed", "#ede9fe", "#4c1d95"),
    "Cypher": ("#0f766e", "#ccfbf1", "#134e4a"),
    "Deadlock": ("#475569", "#e2e8f0", "#1e293b"),
    "Fade": ("#312e81", "#e0e7ff", "#1e1b4b"),
    "Gekko": ("#15803d", "#dcfce7", "#14532d"),
    "Harbor": ("#0369a1", "#e0f2fe", "#0c4a6e"),
    "Iso": ("#1d4ed8", "#dbeafe", "#1e3a8a"),
    "Jett": ("#0891b2", "#cffafe", "#164e63"),
    "KAY/O": ("#1e40af", "#dbeafe", "#172554"),
    "Killjoy": ("#ca8a04", "#fef9c3", "#713f12"),
    "Miks": ("#64748b", "#f1f5f9", "#334155"),
    "Neon": ("#2563eb", "#dbeafe", "#1e3a8a"),
    "Omen": ("#4338ca", "#e0e7ff", "#312e81"),
    "Phoenix": ("#ea580c", "#ffedd5", "#7c2d12"),
    "Raze": ("#f97316", "#ffedd5", "#9a3412"),
    "Reyna": ("#7e22ce", "#f3e8ff", "#581c87"),
    "Sage": ("#0f766e", "#ccfbf1", "#134e4a"),
    "Skye": ("#65a30d", "#ecfccb", "#365314"),
    "Sova": ("#2563eb", "#dbeafe", "#1e3a8a"),
    "Tejo": ("#0f766e", "#ccfbf1", "#134e4a"),
    "Veto": ("#64748b", "#f1f5f9", "#334155"),
    "Viper": ("#166534", "#dcfce7", "#14532d"),
    "Vyse": ("#7c3aed", "#ede9fe", "#4c1d95"),
    "Waylay": ("#be185d", "#fce7f3", "#831843"),
    "Yoru": ("#1d4ed8", "#dbeafe", "#172554"),
}
ROLE_THEMES = {
    "Controller": ("#0f766e", "#99f6e4"),
    "Duelist": ("#b91c1c", "#fdba74"),
    "Initiator": ("#1d4ed8", "#bae6fd"),
    "Sentinel": ("#6d28d9", "#ddd6fe"),
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)


def table_exists(table_name: str) -> bool:
    query = """
        SELECT COUNT(*) AS table_count
        FROM information_schema.tables
        WHERE table_schema = DATABASE()
          AND table_name = %s
    """
    try:
        with get_connection() as conn:
            df = pd.read_sql(query, conn, params=(table_name,))
        return int(df.loc[0, "table_count"]) > 0
    except Exception:
        return False


def safe_read_sql(query: str, params=None) -> tuple[pd.DataFrame, str | None]:
    try:
        with get_connection() as conn:
            return pd.read_sql(query, conn, params=params), None
    except Exception as err:
        return pd.DataFrame(), str(err)


def value_to_text(value):
    if pd.isna(value):
        return "-"
    if isinstance(value, float):
        if math.isfinite(value) and value.is_integer():
            return int(value)
        return round(value, 2)
    return value


def slugify_name(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", str(name).strip().lower()).strip("_")


def get_local_image_path(folder: str, item_name: str) -> str | None:
    if not item_name or not os.path.isdir(folder):
        return None

    target_slug = slugify_name(item_name)
    for file_name in os.listdir(folder):
        full_path = os.path.join(folder, file_name)
        if not os.path.isfile(full_path):
            continue
        stem, extension = os.path.splitext(file_name)
        if extension.lower() not in IMAGE_EXTENSIONS:
            continue
        if slugify_name(stem) == target_slug:
            return full_path
    return None


def get_agent_origin(agent_name: str) -> str:
    return AGENT_ORIGINS.get(agent_name, "Unknown")


def get_agent_name_theme(agent_name: str) -> tuple[str, str, str]:
    return AGENT_NAME_THEMES.get(agent_name, ("#64748b", "#f8fafc", "#0f172a"))


def render_agent_card(row: pd.Series):
    role_name = value_to_text(row["role"])
    primary_color, accent_color = ROLE_THEMES.get(role_name, ("#334155", "#cbd5e1"))
    image_path = get_local_image_path(AGENT_IMAGE_DIR, row["agent_name"])
    label_bg, label_border, label_text = get_agent_name_theme(row["agent_name"])

    with st.container():
        st.markdown(
            f"""
            <div style="
                margin: -0.2rem;
                padding: 0.75rem 0.75rem 0.95rem 0.75rem;
                border-radius: 22px;
                background: transparent;
                border: none;
                box-shadow: none;
            ">
            """,
            unsafe_allow_html=True,
        )

        if image_path:
            image_col_left, image_col_center, image_col_right = st.columns([1, 3, 1])
            with image_col_center:
                st.image(image_path, width=170)
        else:
            st.markdown(
                f"""
                <div style="
                    aspect-ratio: 1 / 1;
                    border-radius: 18px;
                    border: 1px solid rgba(148, 163, 184, 0.25);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
                    font-size: 2rem;
                    font-weight: 700;
                    color: #1e293b;
                ">
                    {row["agent_name"][:2].upper()}
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown(
            f"""
            <div style="margin-top: 0.65rem; color: #0f172a;">
                <div style="
                    display: inline-block;
                    padding: 0.35rem 0.7rem;
                    border-radius: 999px;
                    background: {label_bg};
                    border: 1px solid {label_border};
                    font-size: 1rem;
                    font-weight: 800;
                    letter-spacing: 0.02em;
                    color: {label_text};
                ">
                    {row["agent_name"]}
                </div>
                <div style="font-size: 0.84rem; font-weight: 600; color: {primary_color}; margin-top: 0.18rem;">
                    {role_name}
                </div>
                <div style="font-size: 0.92rem; color: #475569; margin-top: 0.32rem;">
                    Origin: {get_agent_origin(row["agent_name"])}
                </div>
            </div>
            <div style="height: 0.1rem;"></div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def prepare_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    return df.map(value_to_text)


def show_dataframe(title: str, query: str, params=None):
    st.subheader(title)
    df, error = safe_read_sql(query, params=params)
    if error:
        st.error(f"Query failed: {error}")
        return
    if df.empty:
        st.info("No data found.")
        return
    st.dataframe(prepare_dataframe(df), use_container_width=True, hide_index=True)


def show_missing_table(table_name: str):
    st.subheader(table_name.replace("_", " ").title())
    st.warning(f"`{table_name}` table was not found.")
    st.code(MISSING_TABLE_SQL[table_name], language="sql")


def render_agents():
    st.subheader("Agents")
    agents_df, agents_error = safe_read_sql(
        """
        SELECT agent_name, role
        FROM agents
        ORDER BY agent_name
        """
    )
    if agents_error:
        st.error(f"Query failed: {agents_error}")
        return
    if agents_df.empty:
        st.info("No agents found.")
        return

    if not os.path.isdir(AGENT_IMAGE_DIR):
        st.info(f"Agent photos will appear here after adding files to `{AGENT_IMAGE_DIR}`.")

    role_order = ["Controller", "Duelist", "Initiator", "Sentinel"]
    known_roles = agents_df[agents_df["role"].isin(role_order)]
    extra_roles = sorted(role for role in agents_df["role"].dropna().unique() if role not in role_order)
    display_roles = role_order + extra_roles

    for role_name in display_roles:
        role_df = agents_df[agents_df["role"] == role_name]
        if role_df.empty:
            continue

        st.markdown(f"### {role_name}")
        columns = st.columns(4)
        for index, row in role_df.reset_index(drop=True).iterrows():
            with columns[index % 4]:
                with st.container(border=True):
                    render_agent_card(row)

    uncategorized_df = agents_df[agents_df["role"].isna() | (agents_df["role"].astype(str).str.strip() == "")]
    if not uncategorized_df.empty:
        st.markdown("### Uncategorized")
        columns = st.columns(4)
        for index, row in uncategorized_df.reset_index(drop=True).iterrows():
            with columns[index % 4]:
                with st.container(border=True):
                    render_agent_card(row)


def render_overview():
    st.subheader("Database Overview")

    teams_df, teams_error = safe_read_sql("SELECT COUNT(*) AS count FROM teams")
    players_df, players_error = safe_read_sql("SELECT COUNT(*) AS count FROM players")
    agents_df, agents_error = safe_read_sql("SELECT COUNT(*) AS count FROM agents")
    maps_df, maps_error = safe_read_sql("SELECT COUNT(*) AS count FROM maps")
    events_df, events_error = safe_read_sql("SELECT COUNT(*) AS count FROM events") if table_exists("events") else (pd.DataFrame({"count": [0]}), None)

    errors = [err for err in [teams_error, players_error, agents_error, maps_error, events_error] if err]
    if errors:
        st.error(f"Query failed: {errors[0]}")
        return

    match_count = 0
    if table_exists("matches"):
        matches_df, matches_error = safe_read_sql("SELECT COUNT(*) AS count FROM matches")
        if matches_error:
            st.error(f"Query failed: {matches_error}")
            return
        match_count = int(matches_df["count"][0]) if not matches_df.empty else 0

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.metric("Teams", int(teams_df["count"][0]) if not teams_df.empty else 0)
    col2.metric("Players", int(players_df["count"][0]) if not players_df.empty else 0)
    col3.metric("Agents", int(agents_df["count"][0]) if not agents_df.empty else 0)
    col4.metric("Maps", int(maps_df["count"][0]) if not maps_df.empty else 0)
    col5.metric("Events", int(events_df["count"][0]) if not events_df.empty else 0)
    col6.metric("Matches", match_count)


def render_team_players():
    st.subheader("Team Players")
    teams_df, teams_error = safe_read_sql("SELECT team_name FROM teams ORDER BY team_name")
    if teams_error:
        st.error(f"Query failed: {teams_error}")
        return

    if teams_df.empty:
        st.info("No teams found.")
        return

    selected_team = st.selectbox("Select Team", teams_df["team_name"].tolist())
    query = """
        SELECT p.player_name, t.team_name, p.country
        FROM players p
        JOIN teams t ON p.team_id = t.team_id
        WHERE t.team_name = %s
    """
    show_dataframe("Players in Selected Team", query, params=(selected_team,))


def render_advance_query():
    st.subheader("Advance Query")
    option = st.selectbox(
        "Choose Dataset",
        ["Valorant Events", "Matches", "Player Match Stats", "Team Match Stats"],
    )

    if option == "Valorant Events":
        if table_exists("events"):
            show_dataframe(
                "Valorant Events",
                """
                SELECT e.event_id,
                       e.event_name,
                       e.event_prize,
                       e.event_location,
                       e.event_dates,
                       COUNT(m.match_id) AS total_matches
                FROM events e
                LEFT JOIN matches m ON e.event_id = m.event_id
                GROUP BY e.event_id, e.event_name, e.event_prize, e.event_location, e.event_dates
                ORDER BY e.event_id
                """,
            )
        else:
            show_missing_table("events")
    elif option == "Matches":
        if table_exists("matches"):
            events_df, events_error = safe_read_sql(
                """
                SELECT event_id, event_name
                FROM events
                ORDER BY event_name
                """
            )
            if events_error:
                st.error(f"Query failed: {events_error}")
                return

            selected_event = "All Events"
            if not events_df.empty:
                event_options = ["All Events"] + events_df["event_name"].tolist()
                selected_event = st.selectbox("Filter By Event", event_options)

            match_query = """
                SELECT m.match_id,
                       m.event_id,
                       e.event_name,
                       e.event_dates,
                       m.event_stage,
                       m.match_series,
                       m.match_date,
                       m.match_time,
                       COALESCE(mm.map_name, '-') AS map_name,
                       m.team1_id,
                       CASE
                           WHEN m.team1_id IS NOT NULL THEN t1.team_name
                           ELSE CONCAT(m.team1_name, ' (Unlinked)')
                       END AS team1_name,
                       m.team1_score,
                       m.team2_id,
                       CASE
                           WHEN m.team2_id IS NOT NULL THEN t2.team_name
                           ELSE CONCAT(m.team2_name, ' (Unlinked)')
                       END AS team2_name,
                       m.team2_score,
                       m.winner_team_id,
                       CASE
                           WHEN m.winner_team_id IS NOT NULL THEN tw.team_name
                           ELSE CONCAT(m.winner_team_name, ' (Unlinked)')
                       END AS winner_team_name,
                       m.winning_score,
                       m.status
                FROM matches m
                JOIN events e ON m.event_id = e.event_id
                LEFT JOIN (
                    SELECT match_id,
                           GROUP_CONCAT(COALESCE(mp.map_name, mm.map_name) ORDER BY mm.map_number SEPARATOR ', ') AS map_name
                    FROM match_maps mm
                    LEFT JOIN maps mp ON mm.map_id = mp.map_id
                    GROUP BY match_id
                ) mm ON m.match_id = mm.match_id
                LEFT JOIN teams t1 ON m.team1_id = t1.team_id
                LEFT JOIN teams t2 ON m.team2_id = t2.team_id
                LEFT JOIN teams tw ON m.winner_team_id = tw.team_id
            """
            params = None
            if selected_event != "All Events":
                match_query += " WHERE e.event_name = %s"
                params = (selected_event,)
            match_query += " ORDER BY m.match_id ASC"

            show_dataframe(
                "Matches",
                match_query,
                params=params,
            )
        else:
            show_missing_table("matches")
    elif option == "Player Match Stats":
        if table_exists("player_match_stats"):
            show_dataframe(
                "Player Match Stats",
                """
                SELECT pms.player_stat_id,
                       pms.match_id,
                       p.player_name,
                       pms.kills,
                       pms.deaths,
                       pms.assists,
                       pms.acs
                FROM player_match_stats pms
                LEFT JOIN players p ON pms.player_id = p.player_id
                ORDER BY pms.player_stat_id
                """,
            )
        else:
            show_missing_table("player_match_stats")
    else:
        if table_exists("team_match_stats"):
            show_dataframe(
                "Team Match Stats",
                """
                SELECT tms.team_stat_id,
                       tms.match_id,
                       t.team_name,
                       tms.rounds_won,
                       tms.rounds_lost,
                       tms.first_bloods,
                       tms.spike_plants
                FROM team_match_stats tms
                LEFT JOIN teams t ON tms.team_id = t.team_id
                ORDER BY tms.team_stat_id
                """,
            )
        else:
            show_missing_table("team_match_stats")


def main():
    st.set_page_config(page_title="Valorant Database Dashboard", layout="wide")

    st.title("Valorant Database Dashboard")
    st.caption("Streamlit version of your Valorant DB viewer.")

    selected_view = st.sidebar.radio("Navigation", MENU_ITEMS)

    if selected_view == "Overview":
        render_overview()
    elif selected_view == "Teams":
        show_dataframe("Teams", "SELECT * FROM teams")
    elif selected_view == "Players":
        show_dataframe(
            "Players with Teams",
            """
            SELECT p.player_name, t.team_name, p.country
            FROM players p
            JOIN teams t ON p.team_id = t.team_id
            """,
        )
    elif selected_view == "Agents":
        render_agents()
    elif selected_view == "Maps":
        show_dataframe("Maps", "SELECT * FROM maps")
    elif selected_view == "Team Players":
        render_team_players()
    elif selected_view == "Advance Query":
        render_advance_query()


if __name__ == "__main__":
    main()
