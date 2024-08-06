from langchain_ollama import ChatOllama


def get_instance():
    return ChatOllama(
        model="llama3.1:8b-instruct-q8_0",
        temperature=0.5,
        keep_alive=15
    )
