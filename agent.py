from tools import visit_webpage, image_generation_tool, image_diplay_tool
from smolagents import (
    CodeAgent,
    ToolCallingAgent,
    HfApiModel,
    ManagedAgent,
    DuckDuckGoSearchTool
)

def multi_agent_framework(model_id):
    model = HfApiModel(model_id)

    web_agent = ToolCallingAgent(
        tools=[DuckDuckGoSearchTool(), visit_webpage],
        model=model,
        max_steps=5,
    )

    managed_web_agent = ManagedAgent(
        agent=web_agent,
        name="search",
        description="Runs web searches for you. Give it your query as an argument.",
    )

    manager_agent = CodeAgent(
        tools=[image_generation_tool, image_diplay_tool],
        model=model,
        managed_agents=[managed_web_agent],
        additional_authorized_imports=["time", "numpy", "pandas", "requests"],
    )

    return manager_agent