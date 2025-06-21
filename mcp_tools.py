from fastmcp import FastMCP
from tools.diagnosis_tools import get_diagnosis
from tools.symptom_extractor import extract_symptoms
from tools.pubmed_fetcher import fetch_pubmed_articles_with_metadata
from tools.summarizer import summarize_text

mcp = FastMCP("Medical diagnosis custom mcp")



@mcp.tool()
def full_medical_analysis(symptom_text):
    symptoms = extract_symptoms(data.description)
    diagnosis = get_diagnosis(symptoms)
    pubmed_raw = fetch_pubmed_articles_with_metadata(" ".join(symptoms))
    summary = summarize_text(pubmed_raw[:3000])


    return {
        "symptom": symptoms,
        "diagnosis": diagnosis,
        "pubmed_summary": summary
    }




if __name__ == "__main__":
    mcp.run()