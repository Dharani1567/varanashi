from tavily import TavilyClient
import os

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_tavily(query, days=3):
    response = client.search(
        query=query,
        max_results=5,
        days=days
    )
    return response.get("results", [])
