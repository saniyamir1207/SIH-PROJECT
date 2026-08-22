from fastapi import FastAPI
from services.excel_service import get_symptoms, get_questions

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Healthsphere Backend Running"}

@app.get("/symptoms")
def symptoms():
    return get_symptoms()

@app.get("/questions")
def questions():
    return get_questions()