from langchain.schema import SystemMessage
from langgraph.prebuilt import ToolNode

from app import prompt
from tools import RESEARCH_TOOLS_LIST
from app.models import RetrieverState, OrganizerState
from app import retriever_llm_with_tools, transcriber_llm


RESEARCH_TOOLS_NODE = ToolNode(tools=RESEARCH_TOOLS_LIST)


def retriever_node(state: RetrieverState):
    response = retriever_llm_with_tools.invoke(
        [SystemMessage(content=prompt.EXPANDER_PROMPT)] + state["messages"]
    )
    if response.content:
        return {"messages": response, "researched_contents": response.content}
    return {"messages": response}


def organizer_node(state: OrganizerState):
    response = transcriber_llm.invoke(
        [SystemMessage(content=prompt.ORGANIZER_PROMPT)] + state["researched_contents"]
    )
    return {"cleaned_content": response.content}


def podcaster_node(state: OrganizerState):
    response = transcriber_llm.invoke(
        [SystemMessage(content=prompt.PODCASTER_PROMPT)] + state["cleaned_content"]
    )
    return {"transcript": response.content}
