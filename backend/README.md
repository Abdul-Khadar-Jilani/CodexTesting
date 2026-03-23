# DecisionGraph Backend MVP

A FastAPI scaffold for the DecisionGraph project: a multi-agent research and decision intelligence platform built for Supabase persistence and Groq/Gemini model routing.

## Included
- FastAPI API routes for tasks and workflow runs
- LangGraph-ready graph state and node structure
- LLM routing layer for Groq and Gemini
- Supabase repository abstraction with in-memory fallback for local development
- Pydantic schemas for tasks, plans, evidence, critiques, and final memos

## Run locally
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Test
```bash
cd backend
pytest
```
