
class BaseAgent:
    def __init__(self, name, prompt, model="openai/gpt-4"):
        self.name = name
        self.prompt = prompt
        self.model = model

    def process(self, state):
        raise NotImplementedError("Must be implemented in subclass")
