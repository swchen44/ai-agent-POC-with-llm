from core.base_agent import BaseAgent
from core.llm_api import llm_call
from .prompt import prompt

class ModuleDesignAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="ModuleDesigner",
            prompt=prompt,
            model="openai/gpt-4"
        )

    def process(self, state):
        system_design = state.get("system_design")
        if not system_design:
            raise ValueError("Missing 'system_design' in state")

        result = llm_call(self.prompt, system_design)
        state["module_plan"] = result
        return state