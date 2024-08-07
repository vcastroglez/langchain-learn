import os
from exa_py import Exa
from langchain.agents import tool
from langchain_community.utilities import GoogleSerperAPIWrapper
from crewai_tools import GithubSearchTool


class ToolSet:
	@tool
	def search(query: str):
		"""Search for a webpage based on the query."""
		return ToolSet._exa().search(f"{query}", use_autoprompt=True, num_results=3)

	def github_search(self, repository: str):
		return GithubSearchTool(
			github_repo=repository,
			content_types=['code']
		)

	@tool
	def find_similar(url: str):
		"""Search for webpages similar to a given URL.
		The url passed in should be a URL returned from `search`.
		"""
		return ToolSet._exa().find_similar(url, num_results=3)

	@tool
	def get_contents(ids: str):
		"""Get the contents of a webpage.
		The ids must be passed in as a list, a list of ids returned from `search`.
		"""
		eval_ids = eval(ids)

		contents = str(ToolSet._exa().get_contents(eval_ids))
		contents = contents.split("URL:")
		contents = [content[:1000] for content in contents]
		return "\n\n".join(contents)

	@tool
	def search_serper(query: str):
		search = GoogleSerperAPIWrapper()
		return search.run(f"{query}")

	@staticmethod
	def tools():
		return [
			ToolSet.search,
			ToolSet.find_similar,
			ToolSet.get_contents,
			ToolSet.search_serper,
			ToolSet.github_search,
		]

	@staticmethod
	def _exa():
		return Exa(api_key=os.environ.get('EXA_API_KEY'))
