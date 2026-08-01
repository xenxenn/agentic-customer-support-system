from langgraph.prebuilt import create_react_agent

from model import get_model
from tools import calculator
from memory import memory
from knowledge import search_knowledge_base

llm = get_model()

graph = create_react_agent(
    model=llm,
    tools=[
        calculator,
        search_knowledge_base
    ],
    checkpointer=memory,
)