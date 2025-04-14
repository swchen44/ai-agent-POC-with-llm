from core.base_agent import BaseAgent
from core.llm_api import llm_call
from .prompt import prompt

class RequirementAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="RequirementAnalyzer",
            prompt=prompt,
            model="openai/gpt-4"
        )

    def process(self, state):
        user_input = state.get("input")
        if not user_input:
            raise ValueError("Missing input text in state")

        result = llm_call(self.prompt, user_input)
        state["requirements"] = result
        return state