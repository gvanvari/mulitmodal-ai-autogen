import warnings

warnings.filterwarnings("ignore")

import os
import random

from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

from config import llm_config_openai
from prompt import citizen_prompt, initial_task_message, politicians_prompt

load_dotenv()

print("Setup Complete: Libraries installed and API keys loaded.")

politician_agent = AssistantAgent(
    name="Council_Member_OpenAI",
    model_client=OpenAIChatCompletionClient(model="gpt-4o-mini"),
    system_message=politicians_prompt,
)

print(f"Agent '{politician_agent.name}' created (using OpenAI).")

citizen_agent = AssistantAgent(
    name="Citizen_OpenAI",
    model_client=OpenAIChatCompletionClient(model="gpt-4o-mini"),
    system_message=citizen_prompt,
)

print(f"Agent '{citizen_agent.name}' created (using OpenAI).")

# treasury_agent = autogen.ConversableAgent(
#     name = "City_Treasury_Official_OpenAI",
#     system_message = treasury_prompt,
#     llm_config = llm_config_openai,  # Assign the OpenAI config
#     human_input_mode = "NEVER")

# print(f"Agent '{treasury_agent.name}' created (using OpenAI).")

print("--- Starting Agent Conversation (OpenAI Only) ---")
print("Politician starting conversation Max Turns = 4")
print("--------------------------------------------------")

import asyncio

from autogen_agentchat.messages import TextMessage


async def run_conversation():
    # Create initial message
    messages = [TextMessage(content=initial_task_message, source="user")]

    # Simulate conversation with max 4 turns
    for turn in range(4):
        print(f"\n--- Turn {turn + 1} ---")

        # Politician responds
        response = await politician_agent.on_messages(messages, cancellation_token=None)
        messages.append(response.chat_message)
        print(f"\n{politician_agent.name}:\n{response.chat_message.content}\n")

        # Check for termination
        if "TERMINATE" in response.chat_message.content:
            print("Conversation terminated by politician.")
            break

        # Citizen responds
        response = await citizen_agent.on_messages(messages, cancellation_token=None)
        messages.append(response.chat_message)
        print(f"\n{citizen_agent.name}:\n{response.chat_message.content}\n")

        # Check for termination
        if "TERMINATE" in response.chat_message.content:
            print("Conversation terminated by citizen.")
            break


print("\n--------------------------------------------------")
print("--- Conversation Ended (OpenAI Only) ---")

# Run the async conversation
asyncio.run(run_conversation())
