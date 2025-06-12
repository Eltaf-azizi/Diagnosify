import requests
from bs4 import BeautifulSoup


def fetch_pubmed_articles_with_metadata(query: str, max_results=3, use_mock_if_empty=True):
    headers = {"User-agent": "Mozilla/5.0"}


    # Step 1: Search PubMed
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    search_params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json"
    }