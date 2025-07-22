# tools/search_tool.py
from langchain.tools import tool
import requests

@tool
def search_fitness(query: str) -> str:
    """Performs a web search using DuckDuckGo to return a short summary."""
    response = requests.get(f"https://api.duckduckgo.com/?q={query}&format=json")
    if response.status_code == 200:
        return response.json().get("AbstractText", "No summary found.")
    return "Search failed."
