from fastapi import FastAPI

app = FastAPI(title="AI Recruitment Matching System")

@app.get("/health")
def health_check():
    return {"status": "ok"}
