
import pytest
from agents.requirement_agent.agent import RequirementAgent
from agents.system_design_agent.agent import SystemDesignAgent
from agents.module_design_agent.agent import ModuleDesignAgent


@pytest.fixture
def basic_state():
    return {"input": "Add Wi-Fi frame aggregation feature."}


def test_requirement_agent(basic_state):
    agent = RequirementAgent()
    updated = agent.process(basic_state.copy())
    assert "requirements" in updated
    assert isinstance(updated["requirements"], str)


def test_system_agent():
    agent = SystemDesignAgent()
    state = {"requirements": "The system must support Wi-Fi frame aggregation."}
    updated = agent.process(state)
    assert "system_design" in updated
    assert isinstance(updated["system_design"], str)


def test_module_agent():
    agent = ModuleDesignAgent()
    state = {"system_design": "Implement in firmware and partially in kernel."}
    updated = agent.process(state)
    assert "module_plan" in updated
    assert isinstance(updated["module_plan"], str)
