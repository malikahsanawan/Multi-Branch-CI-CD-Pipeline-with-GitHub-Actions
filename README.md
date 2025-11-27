# FastAPI Demo Project

Simple FastAPI application used to demonstrate a GitHub Actions CI workflow.

## Local development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://localhost:8000/docs to explore the auto-generated API docs.

## GitHub Actions CI

A workflow in `.github/workflows/ci.yml` installs dependencies, runs format/type checks, and executes tests on push and pull requests targeting `main`.

