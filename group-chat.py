import warnings

warnings.filterwarnings("ignore")

import asyncio
import os
import random

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

from prompt import citizen_prompt, politicians_prompt, treasury_prompt

load_dotenv()

print("Setup Complete: Libraries installed and API keys loaded.")

# Create the agents
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

print(f"Agent '{politician_agent.name}' created.")
print(f"Agent '{citizen_agent.name}' created.")
print(f"Agent '{treasury_agent.name}' created.")

print("--- Starting Multi-Agent Group Chat (HIL) ---")
print("Politician, Citizen, and Treasury Official discuss budget allocation.")
print("---------------------------------------------------------------------")


async def run_group_chat(rounds:int):
    # Initial task message
    initial_task = TextMessage(
        content="Context: Budget planning committee meeting. Discuss and reach consensus on city budget allocation for the next fiscal year. The citizen wants social programs, the politician wants re-election appeal, and the treasury official wants budget balance.",
        source="user",
    )

    messages = [initial_task]
    agents = [politician_agent, citizen_agent, treasury_agent]

    for round_num in range(rounds):
        print(f"\n--- Round {round_num + 1} ---")
        all_terminated = True

        for agent in agents:
            try:
                response = await agent.on_messages(messages, cancellation_token=None)
                messages.append(response.chat_message)
                print(f"\n{agent.name}:\n{response.chat_message.content}\n")

                # Check if agent wants to terminate
                if "TERMINATE" not in response.chat_message.content.upper():
                    all_terminated = False
            except Exception as e:
                print(f"Error from {agent.name}: {e}")
                all_terminated = False

        # If all agents want to terminate, end the conversation
        if all_terminated:
            print("\nAll agents have reached consensus. Conversation concluded.")
            break

    return messages


print()

# Run the group chat
rounds = 3
messages = asyncio.run(run_group_chat(rounds))

print("---------------------------------------------------------------------")
print("--- Conversation Ended ---")
print(f"Total messages exchanged: {len(messages)}")

print_chat_history(group_chat_result)
