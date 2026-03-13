from serpapi import GoogleSearch
from config.config import SERP_API_KEY

def search_web(query):
    """
    Perform a Google search and return snippets
    """
    try:

        params = {
            "engine": "google",
            "q": query,
            "api_key": SERP_API_KEY,
            "num": 3
        }

        search = GoogleSearch(params)

        results = search.get_dict()

        snippets = []

        if "organic_results" in results:
            for result in results["organic_results"]:
                if "snippet" in result:
                    snippets.append(result["snippet"])

        return " ".join(snippets)

    except Exception as e:
        print(f"Web search error: {e}")
        return ""