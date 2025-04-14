from core.base_agent import BaseAgent
from core.llm_api import llm_call

prompt = """
You are a software reviewer agent. Analyze the module design and evaluate:
1. Does it fulfill the original requirements?
2. Are there architectural issues or missing elements?
3. Suggest improvements or edge cases to consider.
Respond in markdown.
"""

class SelfEvaluationAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="SelfEvaluator",
            prompt=prompt,
            model="openai/gpt-4"
        )

    def process(self, state):
        module_plan = state.get("module_plan")
        if not module_plan:
            raise ValueError("Missing 'module_plan' in state")

        review = llm_call(self.prompt, module_plan)
        state["evaluation"] = review
        return state
