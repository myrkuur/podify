from tools.researchers import *
from tools.audio_editors import *


RESEARCH_TOOLS_LIST = [
    web_searcher(),
    wiki_searcher(),
    # arxiv_searcher(),
    pubmed_searcher(),
    semanticscholar_searcher(),
]


AUDIO_TOOLS_LIST = [tts()]
