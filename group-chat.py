import asyncio
import warnings

warnings.filterwarnings("ignore")

from autogen_agentchat.messages import TextMessage
from dotenv import load_dotenv

from agents import create_agents

load_dotenv()

politician_agent, citizen_agent, treasury_agent = create_agents()


async def run_group_chat(rounds: int):
    """Run multi-agent group chat for specified number of rounds."""
    initial_task = TextMessage(
        content="Context: Budget planning committee meeting. The citizen wants social programs, the politician wants re-election appeal, and the treasury official wants budget balance.",
        source="user",
    )

    conversation_history = [initial_task]
    agents = [politician_agent, citizen_agent, treasury_agent]

    for round_num in range(rounds):
        print(f"\n--- Round {round_num + 1} ---")

        for agent in agents:
            try:
                response = await agent.on_messages(
                    [conversation_history[-1]], cancellation_token=None
                )
                conversation_history.append(response.chat_message)
                print(f"\n{agent.name}:\n{response.chat_message.content}\n")

                if "TERMINATE" in response.chat_message.content.upper():
                    print("\nConversation concluded.")
                    return conversation_history

            except Exception as e:
                print(f"Error from {agent.name}: {e}")

    return conversation_history


if __name__ == "__main__":
    asyncio.run(run_group_chat(rounds=3))

