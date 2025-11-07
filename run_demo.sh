#!/bin/bash
# Simple helper to run backend and frontend in separate terminals (unix-like)
echo "Start backend: uvicorn backend.app:app --reload --port 8000"
echo "Start frontend: streamlit run frontend/app.py"
