from langchain_core.prompts import PromptTemplate, ChatPromptTemplate


def think_template():
    template = """Question: {question}
    Think following these steps:
    - Recall {deep} things that you know related to the subject of the question, from now own defined as SR.
    - Think what have all the SR in common and what they have not in common that relates to the question.
    - Think again about possible hidden variables that you missed.
    - Use the information gathered in the previous steps to infer a possible explanation for the question.
    Answer:"""
    return template


def think_template_prompt():
    return PromptTemplate(template=think_template(), input_variables=["question", "deep"])


def think_template_prompt_format(question, deep=10):
    return think_template_prompt().format(question=question, deep=deep)


def think_simple_messages():
    messages = [
        ("system", "You answer simple questions"),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
    return messages


def think_simple_template_prompt():
    return ChatPromptTemplate.from_messages(messages=think_simple_messages())
