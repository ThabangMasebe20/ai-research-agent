from langchain_community.utilities import WikipediaAPIWrapper, DuckDuckGoSearchAPIWrapper
from langchain_core.tools import tool, Tool
from datetime import datetime

search = DuckDuckGoSearchAPIWrapper()
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)

@tool
def search_tool(query: str) -> str:
    """Search the web for information."""
    return search.run(query)

@tool
def wikipedia_tool(query: str) -> str:
    """Search Wikipedia for information."""
    return api_wrapper.run(query)

def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    return f"Data successfully saved to {filename}"

save_tool = Tool(
    name="save_to_text_file",
    func=save_to_txt,
    description="Save structured research data to a text file."
)




