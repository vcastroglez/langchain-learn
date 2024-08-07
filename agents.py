from textwrap import dedent

from crewai import Agent

from ollama_creator import get_instance
from tools import ExaSearchToolset


class MeetingPrepAgents:
	@staticmethod
	def research_agent():
		return Agent(
			role="Research Specialist",
			goal='Conduct thorough research on people and companies involved in the meeting',
			tools=ExaSearchToolset.tools(),
			backstory=dedent("""\
          As a Research Specialist, your mission is to uncover detailed information
					about the individuals and entities participating in the meeting. Your insights
					will lay the groundwork for strategic meeting preparation."""),
			verbose=True,
			llm=get_instance()
		)

	@staticmethod
	def industry_analysis_agent():
		return Agent(
			role='Industry Analyst',
			goal='Analyze the current industry trends, challenges, and opportunities',
			tools=ExaSearchToolset.tools(),
			backstory=dedent("""\
            As an Industry Analyst, your analysis will identify key trends,
            challenges facing the industry, and potential opportunities that
            could be leveraged during the meeting for strategic advantage."""),
			verbose=True,
			llm=get_instance()
		)

	@staticmethod
	def meeting_strategy_agent():
		return Agent(
			role='Meeting Strategy Advisor',
			goal='Develop talking points, questions, and strategic angles for the meeting',
			tools=ExaSearchToolset.tools(),
			backstory=dedent("""\
            As a Strategy Advisor, your expertise will guide the development of
            talking points, insightful questions, and strategic angles
            to ensure the meeting's objectives are achieved."""),
			verbose=True,
			llm=get_instance()
		)

	@staticmethod
	def summary_and_briefing_agent():
		return Agent(
			role='Briefing Coordinator',
			goal='Compile all gathered information into a concise, informative briefing document',
			tools=ExaSearchToolset.tools(),
			backstory=dedent("""\
            As the Briefing Coordinator, your role is to consolidate the research,
            analysis, and strategic insights."""),
			verbose=True,
			llm=get_instance()
		)
