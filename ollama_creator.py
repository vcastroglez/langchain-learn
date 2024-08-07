import langchain_ollama


def get_instance():
	return langchain_ollama.ChatOllama(
		model="llama3.1:8b-instruct-q8_0",
		temperature=0.5,
		keep_alive=15
	)


def get_llm():
	return langchain_ollama.OllamaLLM(
		model="llama3.1:8b-instruct-q8_0",
		temperature=0.5,
		keep_alive=15
	)
