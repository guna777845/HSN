# hassan-ai

Hassan Tourism AI — a small Flask app that provides a chat UI and trip planning pages for Hassan district.

## Features
- Flask backend serving templates: landing, plan-trip, famous-places, chat.
- Simple LLM integration in brain.py (uses OPENAI_API_KEY from .env).
- Static assets served from /static.

## Quick start (local)
1. Create venv and install:
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

2. Add local secrets (do NOT commit):
   Create a file named `.env` in the project root:
   ```
   OPENAI_API_KEY=sk-...
   ```

3. Run:
   python3 app.py
   Open http://localhost:5001

## Endpoints
- `/` → landing page
- `/plan-trip` → plan_trip.html
- `/famous-places` → famous_places.html
- `/chat` → chat UI (GET) and chat API (POST)

## Deployment (free options)
- Render: connect GitHub repo, set start command `python3 app.py`, add env var in dashboard.
- Railway: connect repo, set environment variables in project settings.
- Fly.io: `fly launch` then `fly deploy`; set secrets with `fly secrets set`.
- PythonAnywhere: create web app, set virtualenv and environment variables.

Configure production secrets via host dashboard — never commit `.env`.

## Security
If an API key was committed, rotate/revoke it immediately and remove .env from git history.

## License

