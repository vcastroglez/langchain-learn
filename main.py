import os

from crewai import Agent
from crewai import Crew
from dotenv import load_dotenv
from exa_py import Exa
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import Tool

from agents import manager_agent, backend_developer_agent, frontend_developer_agent, qa_specialist_agent
from ollama_creator import get_instance
from tasks import TasksStack
from tools import ToolSet


def main():
	load_dotenv()

	print("## Welcome to the Meeting Prep Crew")
	print('-------------------------------')
	app_to_develop = input("What app do you want to develop, state it as an action?\n")

	tasks = TasksStack()
	llm = get_instance()

	exa_wrapper = Exa(api_key=os.environ.get('EXA_API_KEY'))
	exa_tool = Tool(
		name="Search the web",
		func=exa_wrapper.search,
		description="useful for when you need to search information in the web"
	)
	serper_wrapper = GoogleSerperAPIWrapper()
	serper_tool = Tool(
		name="Search the web",
		func=serper_wrapper.run,
		description="useful for when you need to ask with search"
	)

	research_agent_instance = Agent(
		role="Research Specialist",
		goal=f"""Conduct thorough research on {app_to_develop}""",
		tools=[exa_tool, serper_tool],
		backstory=f"""
          As a Research Specialist, your mission is to uncover detailed information
					about {app_to_develop}. Your insights
					will lay the groundwork for development of the solution.""",
		verbose=True,
		llm=llm
	)
	#TODO continue, all good till here

	manager_agent_instance = manager_agent(llm=llm, app_idea=app_to_develop)
	backend_agent_instance = backend_developer_agent(llm=llm, app_idea=app_to_develop)
	frontend_agent_instance = frontend_developer_agent(llm=llm, app_idea=app_to_develop)
	qa_agent_instance = qa_specialist_agent(llm=llm, app_idea=app_to_develop)

	# create tasks
	research_task = tasks.research_task(research_agent_instance, app_to_develop)
	design_task = tasks.design_task(manager_agent_instance, app_to_develop)
	develop_backend_task = tasks.develop_backend_task(backend_agent_instance, app_to_develop)
	develop_frontend_task = tasks.develop_backend_task(frontend_agent_instance, app_to_develop)
	qa_task = tasks.qa_task(qa_agent_instance, app_to_develop)
	writing_code_task = tasks.qa_task(manager_agent, app_to_develop)

	crew = Crew(
		agents=[
			research_agent_instance,
			manager_agent_instance,
			backend_agent_instance,
			frontend_agent_instance,
			qa_agent_instance,
		],
		tasks=[
			research_task,
			design_task,
			develop_backend_task,
			develop_frontend_task,
			qa_task,
			writing_code_task,
		]
	)

	result = crew.kickoff()

	print(result)


if __name__ == "__main__":
	main()
