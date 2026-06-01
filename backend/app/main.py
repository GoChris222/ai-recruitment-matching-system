from fastapi import FastAPI

from app.models.candidate import Candidate
from app.models.vacancy import Vacancy

from app.services.data_store import load_json, save_json
from app.services.matching_engine import match_candidates_to_vacancy


app = FastAPI(title="AI Recruitment Matching System")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/candidates")
def get_candidates():
    return load_json("candidates.json")


@app.get("/vacancies")
def get_vacancies():
    return load_json("vacancies.json")


@app.post("/vacancies")
def create_vacancy(vacancy: Vacancy):
    vacancies = load_json("vacancies.json")

    vacancies.append(vacancy.model_dump())

    save_json("vacancies.json", vacancies)

    return vacancy


@app.post("/match")
def match_vacancy(vacancy: Vacancy):
    candidates_raw = load_json("candidates.json")

    candidates = [
        Candidate(**candidate)
        for candidate in candidates_raw
    ]

    matches = match_candidates_to_vacancy(
        vacancy,
        candidates
    )

    return matches
