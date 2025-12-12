import asyncio

import gradio as gr
from autogen_agentchat.messages import TextMessage
from dotenv import load_dotenv

from agents import create_agents

load_dotenv()

politician_agent, citizen_agent, treasury_agent = create_agents()

conversation_state = {
    "history": [],
    "agents": [politician_agent, citizen_agent, treasury_agent],
    "current_round": 0,
    "max_rounds": 3,
    "terminated": False,
}


async def run_one_round():
    """Run one round of agent responses."""
    conversation_history = conversation_state["history"]

    if not conversation_history:
        initial_task = TextMessage(
            content="Context: Budget planning committee meeting. The citizen wants social programs, the politician wants re-election appeal, and the treasury official wants budget balance.",
            source="user",
        )
        conversation_history.append(initial_task)

    round_responses = []

    for agent in conversation_state["agents"]:
        try:
            response = await agent.on_messages(
                [conversation_history[-1]], cancellation_token=None
            )
            conversation_history.append(response.chat_message)
            round_responses.append(f"{agent.name}: {response.chat_message.content}")

            if "TERMINATE" in response.chat_message.content.upper():
                conversation_state["terminated"] = True

        except Exception as e:
            round_responses.append(f"Error from {agent.name}: {str(e)}")

    conversation_state["history"] = conversation_history
    conversation_state["current_round"] += 1

    return "\n\n".join(round_responses) if round_responses else "No responses generated."


def get_conversation_display():
    """Get the full conversation history for display."""
    if not conversation_state["history"]:
        return "No conversation yet. Type a message to start."

    display_text = "=== CONVERSATION HISTORY ===\n\n"
    for msg in conversation_state["history"]:
        display_text += f"{msg.source.upper()}: {msg.content}\n\n"
        display_text += "-" * 80 + "\n"

    display_text += f"\nRounds completed: {conversation_state['current_round']}/{conversation_state['max_rounds']}"
    if conversation_state["terminated"]:
        display_text += " (TERMINATED)"

    return display_text


def submit_message(user_input):
    """Process user message and run agent responses."""
    if not user_input.strip():
        return get_conversation_display(), ""

    if conversation_state["terminated"]:
        return get_conversation_display(), "Chat has been terminated."

    if conversation_state["current_round"] >= conversation_state["max_rounds"]:
        return get_conversation_display(), "Maximum rounds reached."

    # Add human message
    human_message = TextMessage(content=user_input, source="human")
    conversation_state["history"].append(human_message)

    # Run one round of agents
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    agent_responses = loop.run_until_complete(run_one_round())
    loop.close()

    status = ""
    if conversation_state["terminated"]:
        status = "Agents reached consensus. Conversation ended."
    elif conversation_state["current_round"] >= conversation_state["max_rounds"]:
        status = "Maximum rounds reached."

    return get_conversation_display(), agent_responses


def terminate_chat():
    """Terminate the chat."""
    conversation_state["terminated"] = True
    return get_conversation_display(), "Chat terminated."


def create_interface():
    with gr.Blocks(title="Multi-Agent Group Chat") as demo:
        gr.Markdown(
        """
        # 🎯 Multi-Agent Budget Discussion
        
        ## Three AI agents discuss city budget allocation:
        **Council Member**, **Citizen**, **Treasury Official**
        
        **How it works:** Type a message to join the discussion. 
        Agents will respond in one round. 
        Repeat until you terminate or 3 rounds complete.
        """
        )
        response_display = gr.Textbox(
            label="Agent Responses",
            lines=6,
            max_lines=10,
            interactive=False,
        )

        with gr.Row():
            user_input = gr.Textbox(
                label="Your Message",
                placeholder="Type something to the agents...",
                lines=2,
            )

        with gr.Row():
            submit_btn = gr.Button("Submit", variant="primary", size="lg")
            terminate_btn = gr.Button("Terminate Chat", variant="stop", size="lg")

        conversation_display = gr.Textbox(
            label="Conversation History",
            value=get_conversation_display(),
            lines=6,
            max_lines=10,
            interactive=False,
        )

        submit_btn.click(
            submit_message,
            inputs=user_input,
            outputs=[conversation_display, response_display],
        ).then(lambda: "", outputs=user_input)

        terminate_btn.click(
            terminate_chat,
            outputs=[conversation_display, response_display],
        )

    return demo


if __name__ == "__main__":
    demo = create_interface()
    demo.launch(share=False, server_name="127.0.0.1", server_port=7860)