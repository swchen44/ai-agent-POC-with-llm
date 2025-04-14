from agents.requirement_agent.agent import RequirementAgent
from agents.system_design_agent.agent import SystemDesignAgent
from agents.module_design_agent.agent import ModuleDesignAgent


def run_pipeline(user_input):
    state = {"input": user_input}

    for agent_cls in [RequirementAgent, SystemDesignAgent, ModuleDesignAgent]:
        agent = agent_cls()
        print(f"\n🚀 Running agent: {agent.name}")
        state = agent.process(state)
        print(f"✅ {agent.name} output:\n", state[list(state.keys())[-1]][:500])

    return state