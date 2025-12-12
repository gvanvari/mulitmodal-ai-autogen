# Multimodal AI - Multi-Agent Conversation System

A sophisticated multi-agent conversation system that simulates realistic budget allocation discussions between political, citizen, and treasury representatives using AI agents powered by OpenAI's language models.

<img width="1083" height="540" alt="Screenshot 2025-12-11 at 9 43 05 PM" src="https://github.com/user-attachments/assets/6f3fc20f-6e40-4ed6-9896-70ffeef020d3" />

## AI Concepts Learned

1. **Multi-Agent Systems** - Multiple autonomous agents with distinct personalities interact through shared message history
2. **Conversational AI** - Agents maintain context across turns and generate coherent responses
3. **System Prompts** - Instructions that define agent behavior and objectives
4. **Async Programming** - Non-blocking concurrent API calls for multiple agents using async/await
5. **Message Protocols** - Standardized TextMessage format with source attribution for agent communication
6. **Consensus Building** - Agents with opposing views reach compromise through dialogue
7. **Prompt Engineering** - Crafting detailed system messages to guide AI behavior
8. **Conversation Flow** - Round-based management with termination conditions and error handling

## Libraries Used

| Library                 | Purpose                            | Key Components                                                |
| ----------------------- | ---------------------------------- | ------------------------------------------------------------- |
| **pyautogen** (v0.10.0) | Multi-agent framework by Microsoft | `AssistantAgent`, `TextMessage`, `OpenAIChatCompletionClient` |
| **openai**              | OpenAI API client                  | GPT-4o-mini language model provider                           |
| **python-dotenv**       | Environment variable management    | `.env` file loading for API keys                              |
| **asyncio**             | Asynchronous I/O                   | Concurrent agent API calls with async/await                   |
| **isort** & **black**   | Code formatting                    | Import organization and style consistency                     |

## Project Files

| File            | Description                                                                    |
| --------------- | ------------------------------------------------------------------------------ |
| `two-way.py`    | 2-agent system (Politician, Citizen) - 4 turns, sequential responses           |
| `group-chat.py` | 3-agent system (Politician, Citizen, Treasury) - 3 rounds, consensus detection |
| `prompt.py`     | System prompts for all agents and initial task context                         |
| `config.py`     | OpenAI API configuration and environment setup                                 |
| `helper.py`     | Utility functions for output formatting                                        |

## Installation & Usage

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run two-agent conversation
python two-way.py

# Run three-agent conversation
python group-chat.py
```

## Requirements

- Python 3.9+
- OpenAI API key (stored in .env file)
- See `requirements.txt` for complete dependencies
