# Valorant Database

This repository contains a Valorant data exploration project written in Python.

## What’s included

- `app.py` — main application logic
- `load_matches.py` — match data loading and processing
- `download_agent_photos.py` — downloads Valorant agent images
- `requirements.txt` — Python dependencies
- `Players/` — player datasets
- `teams/` — team datasets and logos
- `agents/photos/` — agent image assets

## Setup

1. Create a Python virtual environment:
   ```bash
   python -m venv .venv
   ```
2. Activate the environment:
   - Windows PowerShell:
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   - Windows Command Prompt:
     ```cmd
     .\.venv\Scripts\activate.bat
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Run

```bash
python app.py
```

## Notes

- Sensitive values should be stored in `.env`, which is ignored by Git.
- Compiled Python files and cache directories are removed from the repository.
- If you want to add a demo video or dataset, keep large files under version control only if necessary.
