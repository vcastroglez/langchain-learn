from dotenv import load_dotenv
from crewai import Crew

from ollama_creator import get_instance
from tasks import TasksStack
from agents import AgentsHiring


def main():
	load_dotenv()

	llm = get_instance()
	print("## Welcome to the Meeting Prep Crew")
	print('-------------------------------')
	app_to_develop = input("What app do you want to develop, state it as an action?\n")

	tasks = TasksStack()
	agents = AgentsHiring(app_idea=app_to_develop)

	# create tasks
	research_task = tasks.research_task(agents.research_agent(), app_to_develop)
	design_task = tasks.design_task(agents.manager_agent(), app_to_develop)
	develop_backend_task = tasks.develop_backend_task(agents.backend_developer_agent(), app_to_develop)
	develop_frontend_task = tasks.develop_backend_task(agents.frontend_developer_agent(), app_to_develop)
	qa_task = tasks.qa_task(agents.qa_specialist_agent(), app_to_develop)
	writing_code_task = tasks.qa_task(agents.manager_agent(), app_to_develop)

	crew = Crew(
		agents=[
			agents.research_agent(),
			agents.backend_developer_agent(),
			agents.frontend_developer_agent(),
			agents.qa_specialist_agent(),
			agents.manager_agent(),
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
