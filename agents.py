from textwrap import dedent
from crewai import Agent
from tools import ToolSet


def research_agent(llm, app_idea: str):
	agent = Agent(
		role="Research Specialist",
		goal=f"""Conduct thorough research on {app_idea}""",
		tools=[
			ToolSet.search,
			ToolSet.find_similar,
			ToolSet.get_contents,
			ToolSet.search_serper,
			ToolSet.github_search,
		],
		backstory=f"""
          As a Research Specialist, your mission is to uncover detailed information
					about {app_idea}. Your insights
					will lay the groundwork for development of the solution.""",
		verbose=True,
		llm=llm
	)
	return agent


def tech_leader_agent(llm, app_idea):
	return Agent(
		role='Tech leader',
		goal="""Delegate tasks to the tech team developers, help the team on decision making and report to the
				 manager the status of development, develop both frontend as backed.""",
		tools=ToolSet.tools(),
		backstory="""As a tech team leader you are sure of your capabilities and can make final decisions 
			which are hard to others, you decide on what tools to use, what patterns and principles to implement and 
			how to connect all the parts of the solution.""",
		verbose=True,
		allow_delegation=True,
		llm=llm
	)


def backend_developer_agent(llm, app_idea):
	return Agent(
		role='Senior Backend developer',
		goal='Develop the application backend which will be used by the frontend developer.',
		tools=ToolSet.tools(),
		backstory=dedent("""
			You're a senior backend developer, specialized in PHP, you know in detail the principle design patterns
			of the industry and how to apply them.
			"""),
		verbose=True,
		llm=llm
	)


def frontend_developer_agent(llm, app_idea):
	return Agent(
		role='Senior Frontend developer',
		goal='Develop the application frontend which will connect to the code created by the backend developer.',
		tools=ToolSet.tools(),
		backstory=dedent("""
			You're a senior frontend developer, specialized in javascript, you know in detail the principle design patterns
			of the industry and how to apply them.
			"""),
		verbose=True,
		llm=llm
	)


def qa_specialist_agent(llm, app_idea):
	return Agent(
		role='Senior QA specialist',
		goal='Check that the application code generated work as intended and no major flaws exist.',
		tools=ToolSet.tools(),
		backstory=dedent("""
			You're a senior QA specialist, you know how to detect possible bugs and how to communicate it to the 
			developers in a clear manner so that they can fix them.
			"""),
		allow_delegation=True,
		verbose=True,
		llm=llm
	)


def manager_agent(llm, app_idea):
	return Agent(
		role='Team manager',
		goal="""Write the steps necessary to turn an idea of an application to real steps that can be followed to
			have a working product""",
		tools=ToolSet.tools(),
		backstory=dedent("""
			You can take a general idea and turn it to a clear list of tasks and priorities, you know which team
			member is the best match to solve each task and how to turn all the information to concrete results.
			"""),
		allow_delegation=True,
		verbose=True,
		llm=llm
	)
