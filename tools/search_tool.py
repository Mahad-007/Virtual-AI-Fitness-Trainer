# tools/search_tool.py
from langchain.tools import DuckDuckGoSearchRun, Tool

search_tool = DuckDuckGoSearchRun()
search_fitness = Tool(
    name="search_fitness",
    func=search_tool.run,
    description="Search the web for fitness queries using DuckDuckGo and answer in English answer only what is asked ."
)
