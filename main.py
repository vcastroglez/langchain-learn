from dotenv import load_dotenv
from langchain.agents import create_tool_calling_agent, AgentExecutor

from ollama_creator import get_instance
from templates import think_simple_template_prompt

load_dotenv()


def write_log(text):
    with open('output.log', 'a') as myfile:
        myfile.write(text + "\n")


write_log("===============================")
llm = get_instance()

tools = []
agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=think_simple_template_prompt(),
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
answer = agent_executor.invoke({"input": "How much is PI squared"})
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
