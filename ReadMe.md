# AI Research Agent 

An AI-powered research assistant built with LangChain, LangGraph, and Claude (Anthropic). 
The agent can search the web, query Wikipedia, and save research results to a text file.

## Features
- Web search using DuckDuckGo
- Wikipedia lookup
- Saves research output to a text file
- Structured responses using Pydantic

## Tech Stack
- Python 3.x
- LangChain / LangGraph
- Anthropic Claude (claude-3-5-sonnet-20241022)
- DuckDuckGo Search
- Wikipedia API

## Setup

### 1. Clone the repository
git clone https://github.com/ThabangMasebe20/ai-research-agent.git
cd ai-research-agent

### 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

### 3. Install dependencies
pip install -r requirements.txt

### 4. Set up environment variables
Copy .env.example to .env and add your API key:
ANTHROPIC_API_KEY=your_api_key_here

### 5. Run the agent
python main.py

## Usage
When prompted, type your research query and the agent will:
1. Search the web and Wikipedia
2. Generate a structured research response
3. Save the output to research_output.txt

## Project Structure
ai-research-agent/
├── main.py          # Main agent logic
├── tools.py         # Agent tools (search, wikipedia, save)
├── requirements.txt # Project dependencies
├── .env.example     # Example environment variables
└── .gitignore       # Files to ignore in git
```

---

**2. .env.example**
```
ANTHROPIC_API_KEY=your_api_key_here
```

---

**3. .gitignore**
```
.env
venv/
__pycache__/
*.pyc
*.txt
research_output.txt
```

---

**4. requirements.txt**
Make sure it's up to date with everything you installed:
```
langchain
langchain-community
langchain-anthropic
langchain-openai
langchain-core
langgraph
python-dotenv
pydantic
wikipedia
ddgs
duckduckgo-search