from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import PydanticOutputParser
from langgraph.prebuilt import create_react_agent
from tools import search_tool, wikipedia_tool, save_tool

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

tools = [search_tool, wikipedia_tool, save_tool]

agent_executor = create_react_agent(
    model=llm,
    tools=tools,
    prompt=f"""You are a research assistant that will help generate a research paper.
    Answer the user query and use necessary tools.
    Wrap the output in this format and provide no other text:
    {parser.get_format_instructions()}"""
)

query = input("What can I help your research?\n")

raw_response = agent_executor.invoke({
    "messages": [("human", query)]
})

print(raw_response)

try:
    response_text = raw_response["messages"][-1].content
    structured_response = parser.parse(response_text)
    print(structured_response)
except Exception as e:
    print(f"Error: {e} Raw Response - {raw_response}")