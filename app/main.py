from langgraph.graph import StateGraph, START
from langgraph.prebuilt import tools_condition

from app.models import RetrieverState, OrganizerState
from app.nodes import (
    retriever_node,
    organizer_node,
    podcaster_node,
    RESEARCH_TOOLS_NODE,
)

graph_builder = StateGraph(RetrieverState)
graph_builder.add_node("retriever", retriever_node)
graph_builder.add_node("tools", RESEARCH_TOOLS_NODE)
graph_builder.add_conditional_edges("retriever", tools_condition)
graph_builder.add_edge(START, "retriever")
graph_builder.add_edge("tools", "retriever")

subgraph = graph_builder.compile()

graph_builder2 = StateGraph(OrganizerState)
graph_builder2.add_node("organizer", organizer_node)
graph_builder2.add_node("podcaster", podcaster_node)
graph_builder2.add_edge("organizer", "podcaster")

graph_builder2.add_node("retriever_subgraph", subgraph)
graph_builder2.add_edge("retriever_subgraph", "organizer")

graph_builder2.set_entry_point("retriever_subgraph")

graph = graph_builder2.compile()
