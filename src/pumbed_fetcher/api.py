import requests
import json

class PubMedAPI:
    BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

    def __init__(self, email, debug=False):
        """Initialize the PubMed API with user email."""
        self.email = email
        self.debug = debug

    def fetch_papers(self, query, max_results=10):
        """Search for papers based on a query."""
        search_url = f"{self.BASE_URL}esearch.fcgi"
        params = {
            "db": "pubmed",
            "term": query,
            "retmode": "json",
            "retmax": max_results,
            "email": self.email
        }
        if self.debug:
            print(f"Fetching papers with query: {query}")
        response = requests.get(search_url, params=params)
        response.raise_for_status()  # Raise an error if the request fails
        data = response.json()
        return data.get("esearchresult", {}).get("idlist", [])

    def fetch_paper_details(self, paper_ids):
        """Fetch paper details from PubMed given a list of IDs."""
        if not paper_ids:
            return {}

        summary_url = f"{self.BASE_URL}esummary.fcgi"
        params = {
            "db": "pubmed",
            "id": ",".join(paper_ids),
            "retmode": "json",
            "email": self.email
        }
        if self.debug:
            print(f"Fetching details for paper IDs: {paper_ids}")
        response = requests.get(summary_url, params=params)
        response.raise_for_status()  # Raise an error if the request fails
        data = response.json()
        return data.get("result", {})

# ✅ Add wrapper functions for CLI usage
def fetch_papers(query, max_results=10, debug=False):
    """Wrapper function to fetch paper IDs."""
    api = PubMedAPI(email="your_email@example.com", debug=debug)  # Replace with your email
    return api.fetch_papers(query, max_results)

def fetch_paper_details(paper_id, debug=False):
    """Wrapper function to fetch details of a single paper."""
    api = PubMedAPI(email="your_email@example.com", debug=debug)  # Replace with your email
    details = api.fetch_paper_details([paper_id])
    return details.get(str(paper_id), {})

# Example usage (for testing)
if __name__ == "__main__":
    pubmed = PubMedAPI(email="your_email@example.com", debug=True)
    papers = pubmed.fetch_papers("machine learning", max_results=5)
    details = pubmed.fetch_paper_details(papers)
    print(json.dumps(details, indent=2))





