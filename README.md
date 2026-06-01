# AI Recruitment Matching System

## Overview

AI-powered GP locum recruitment matching system.

Features:
- Candidate intelligence profiles
- Vacancy ingestion
- Matching engine
- Suitability scoring
- JSON-based storage
- FastAPI backend

## Tech Stack

- Python
- FastAPI
- Pydantic
- JSON Storage

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run server:

```bash
uvicorn app.main:app --reload
```

## API Endpoints

### Health Check

GET `/health`

### Candidates

GET `/candidates`

### Vacancies

GET `/vacancies`

POST `/vacancies`

### Match Candidates

POST `/match`
