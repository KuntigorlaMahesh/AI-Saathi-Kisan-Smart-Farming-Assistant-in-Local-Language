<<<<<<< HEAD
# AI-Saathi-Kisan-Smart-Farming-Assistant-in-Local-Language
AI SAATHI CHALLENGE HACKATHON
=======
# AI Saathi Kisan — Prototype (Hackathon Starter)

This repository contains a minimal prototype for **AI Saathi Kisan** — a multilingual AI assistant for farmers.
It includes a FastAPI backend and a Streamlit frontend, sample data (weather/market/crop rules), and instructions
to run locally for hackathon demos.

## What’s inside
- `backend/` — FastAPI app with `/api/chat` endpoint (uses a stubbed AI response you can replace with OpenAI).
- `frontend/` — Streamlit UI for quick demos.
- `data/` — sample `market.csv` and `crop_rules.json`.
- `requirements.txt` — Python dependencies.
- `.env.example` — example environment variables.

## Quickstart (Local)
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # mac/linux
   venv\Scripts\activate    # windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run backend:
   ```bash
   uvicorn backend.app:app --reload --port 8000
   ```

4. In a new terminal, run frontend:
   ```bash
   streamlit run frontend/app.py
   ```

5. Open the Streamlit UI (usually at http://localhost:8501) and interact with the demo.

## Replace the AI backend
The backend contains a placeholder function `call_openai_chat` — replace it with actual OpenAI or HF code,
and add API keys to `.env`.

## Demo notes
- The project uses mock weather and market data for the hackathon demo (easy to replace with real APIs).
- Translation functions are mocked — for hackathon, demonstrate bilingual behaviour by toggling `language` field.

Good luck — if you want, I can push this to a GitHub repo or prepare the slide deck next.
>>>>>>> 17cc33c (Initial commit - AI Saathi Kisan prototype)
