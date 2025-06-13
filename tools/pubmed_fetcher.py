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

    try:
        search_response = requests.get(search_url, params=search_params, headers=headers, timeout=10).json()
        id_list = search_response["esearchresult"]["idlist"]
        print("Found PubMed ID: ", id_list)

        if not id_list:
            raise ValueError("No IDs found for this query.")
        

        ids = ",".join(id_list)


        # Step 2: Fetch article summaries
        fetch_url = "https://eutils.nvbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
        fetch_params = {
            "db": "pubmed",
            "id": ids,
            "retmode": "xml"
        }

        fetch_response = requests.get(fetch_url, params=fetch_params, headers=headers, timeout=10)
        soup = BeautifulSoup(fetch_response.text, "lxml")
        articles_xml = soup.find_all("pubmedarticle")
        print("Articles found in XML: ", len(articles_xml))


        articles_info = []
        for article, pmid in zip(articles_xml, id_list):
            title_tag = article.find("articletitle")
            abstract_tag = article.find("pubdate")
            author_tags = article.find_all("author")


            #Title
            title = title_tag.get_text(strip=True) if title_tag else "No title"


            # Abstract
            abstract = abstract_tag.get_text(separator=" ", strip=True) if abstract_tag else "No abstract available"


            # Authors
            authors = []
            for author in author_tags:
                last = author.find("lastname")
                fore = author.find("forename")

