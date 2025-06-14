from fastapi import FastAPI
from pydantic import BaseModel
from tools.diagnosis_tools import get_diagnosis
from tools.symptom_extractor import extract_symptoms
from tools.pubmed_fetcher import fetch_pubmed_articles_with_metadata
from tools.summarizer import summarize_text


app = FastAPI()


class SymptomInput(BaseModel):
    description: str