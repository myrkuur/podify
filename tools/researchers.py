from typing import Literal

from langchain_tavily import TavilySearch
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.utilities import ArxivAPIWrapper
from langchain_community.tools.pubmed.tool import PubmedQueryRun
from langchain_community.tools.semanticscholar.tool import SemanticScholarQueryRun


def web_searcher(
    max_results=3,
    time_range: Literal["day", "week", "month", "year"] = "year",
    search_depth: Literal["basic", "advanced"] = "basic",
):
    tavily = TavilySearch(
        max_results=max_results,
        topic="general",
        search_depth=search_depth,
        time_range=time_range,
    )
    return tavily


def wiki_searcher():
    wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    return wikipedia


def arxiv_searcher():
    arxiv = ArxivAPIWrapper()
    return arxiv


def pubmed_searcher():
    pubmed = PubmedQueryRun()
    return pubmed


def semanticscholar_searcher():
    semanticscholar = SemanticScholarQueryRun()
    return semanticscholar
