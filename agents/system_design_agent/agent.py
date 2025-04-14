from core.base_agent import BaseAgent
from core.llm_api import llm_call
from .prompt import prompt

class SystemDesignAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="SystemDesigner",
            prompt=prompt,
            model="openai/gpt-4"
        )

    def process(self, state):
        requirements = state.get("requirements")
        if not requirements:
            raise ValueError("Missing 'requirements' in state")

        result = llm_call(self.prompt, requirements)
        state["system_design"] = result
        return state