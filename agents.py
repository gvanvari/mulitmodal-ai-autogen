"""Shared agent creation module."""

from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

from prompt import citizen_prompt, politicians_prompt, treasury_prompt


def create_agents():
    """Create and return the three agents."""
    politician_agent = AssistantAgent(
        name="Council_Member",
        model_client=OpenAIChatCompletionClient(model="gpt-4o-mini"),
        system_message=politicians_prompt,
    )

    citizen_agent = AssistantAgent(
        name="Citizen",
        model_client=OpenAIChatCompletionClient(model="gpt-4o-mini"),
        system_message=citizen_prompt,
    )

    treasury_agent = AssistantAgent(
        name="City_Treasury_Official",
        model_client=OpenAIChatCompletionClient(model="gpt-4o-mini"),
        system_message=treasury_prompt,
    )

    return politician_agent, citizen_agent, treasury_agent
