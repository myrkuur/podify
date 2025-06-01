from langchain.chat_models import init_chat_model

from tools import RESEARCH_TOOLS_LIST


RETRIEVER_MODEL_NAME = "gpt-4.1-mini-2025-04-14"
TRANSCRIBER_MODEL_NAME = "claude-sonnet-4-20250514"


retriever_llm = init_chat_model(model=RETRIEVER_MODEL_NAME, temperature=0.1)

transcriber_llm = init_chat_model(model=TRANSCRIBER_MODEL_NAME, temperature=0.1)

retriever_llm_with_tools = retriever_llm.bind_tools(RESEARCH_TOOLS_LIST)
