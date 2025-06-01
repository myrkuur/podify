from typing import Annotated, TypedDict

from langgraph.graph.message import add_messages


class RetrieverState(TypedDict):
    messages: Annotated[list, add_messages]
    researched_contents: str


class OrganizerState(TypedDict):
    researched_contents: str
    cleaned_content: str
    transcript: str

# TODO: rest of tts parameters