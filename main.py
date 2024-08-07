from dotenv import load_dotenv
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.chains.conversation.base import ConversationChain
from langchain.chains.llm import LLMChain
from langchain.chains.llm_math.base import LLMMathChain
from langchain.tools import StructuredTool
from langchain_core.output_parsers import StrOutputParser

from ollama_creator import get_instance
from templates import think_simple_template_prompt, think_math_template_prompt

load_dotenv()


def write_log(text):
    with open('output.log', 'a') as my_file:
        my_file.write(text + "\n")


write_log("===============================")
llm = get_instance()
# 
# conversation = ConversationChain(llm=llm, verbose=True)
# conversation.predict(input="Hi there!")
# conversation.predict(input="Can we talk about AI?")
# conversation.predict(input="I'm interested in Reinforcement Learning.")
# 
# 

# 
# question = "Can Barack Obama have a conversation with George Washington?"
# chain = think_simple_template_prompt() | llm | StrOutputParser()
# answer = chain.invoke({'input': question})
# print(answer)
# tools = []
# agent = create_tool_calling_agent(
#     llm=llm,
#     tools=tools,
#     prompt=think_math_template_prompt(),
# )
# 
# agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
# answer = agent_executor.invoke({"input": "How much is 2 + 5"})
# write_log(answer['output'])

# chain = think_simple_template_prompt() | get_instance() | StrOutputParser()
# answer = chain.invoke("why is the sky blue?")
# write_log(answer)

# write_log("==========================================================")
# llm = get_instance()
# answer = llm.invoke(think_template("Why is the night sky dark?", 3))
# 
# write_log(answer.content)
# llm = get_instance()
# 
# messages = [
#     (
#         "human",
#         think_template("Why is the blood red?")
#     )
# ]
# answer = llm.invoke(messages)
# print(answer)

# messages = [
#     (
#         "system",
#         "You are a helpful assistant that translates English to French. Translate the user sentence.",
#     ),
#     ("human", "I love programming."),
# ]
# 
# ai_msg = llm.invoke(messages)
# print(ai_msg)
