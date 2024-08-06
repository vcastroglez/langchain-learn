from langchain_core.output_parsers import StrOutputParser
from ollama_creator import get_instance
from templates import think_template_prompt, think_simple_template_prompt
from dotenv import load_dotenv
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import load_tools, create_tool_calling_agent, AgentExecutor

load_dotenv()
search = GoogleSerperAPIWrapper()


def write_log(text):
    with open('output.log', 'a') as myfile:
        myfile.write(text + "\n")


write_log("===============================")
llm = get_instance()
tools = load_tools(["wikipedia", "llm-math"], llm=llm)
agent = create_tool_calling_agent(llm, tools, think_simple_template_prompt())

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
answer = agent_executor.invoke({"question": "In what year was the film Departed with Leonardo Dicaprio released? "
                                            "What is this year raised to the 0.43 power?"})
print(answer)



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
