# Multimodal AI - Multi-Agent Conversation System

A sophisticated multi-agent conversation system that simulates realistic budget allocation discussions between political, citizen, and treasury representatives using AI agents powered by OpenAI's language models.

## AI Concepts Learned

### 1. **Multi-Agent Systems (MAS)**

- Architecture where multiple autonomous agents interact and collaborate
- Each agent operates independently with its own system message/personality
- Agents communicate through shared message history
- Enables complex problem-solving through agent cooperation

### 2. **Conversational AI / Chat-Based Interfaces**

- Agents maintain conversation context through message history
- Each turn involves processing previous messages and generating contextual responses
- Natural dialogue flow simulating human-like conversations
- Context awareness across multiple turns

### 3. **Agent Personas & System Prompts**

- **System Message**: Instructions that define agent behavior and personality
- Each agent has distinct objectives (Politician: re-election, Citizen: social programs, Treasury: budget balance)
- System prompts guide responses without explicit programming of logic
- Enables role-playing and perspective-taking in AI

### 4. **Asynchronous Programming for LLM Calls**

- Using async/await to handle concurrent API calls to language models
- Non-blocking I/O for better performance with multiple agents
- Handling concurrent agent responses efficiently
- Proper cancellation token management

### 5. **Message-Based Communication Protocol**

- Standardized message format (TextMessage) for inter-agent communication
- Message source attribution (who sent each message)
- Message history as shared context for all agents
- Sequential message appending for conversation continuity

### 6. **Conversation Flow Control**

- Round-based conversation management (max rounds/turns)
- Termination conditions (explicit TERMINATE signals)
- Turn allocation among multiple agents
- Error handling in multi-agent scenarios

## Libraries Used

### Core AI/ML Libraries

#### **pyautogen** (v0.10.0)

- **Purpose**: Multi-agent conversation framework by Microsoft
- **Key Components Used**:
  - `autogen_agentchat.agents.AssistantAgent`: Creates autonomous AI agents with system messages
  - `autogen_agentchat.messages.TextMessage`: Standardized message format for agent communication
  - `autogen_agentchat.messages.Response`: Response wrapper containing agent outputs
  - `autogen_ext.models.openai.OpenAIChatCompletionClient`: OpenAI API integration client

#### **openai** (latest)

- **Purpose**: Official Python client for OpenAI API
- **Usage**: Backend language model provider (GPT-4o-mini)
- **Features**: Token management, API authentication, chat completion calls

## Project Files

### `two-way.py`

Two-agent conversation system demonstrating politician-citizen dialogue on budget allocation.

- **Agents**: Politician, Citizen
- **Turns**: 4 maximum rounds
- **Mode**: Sequential agent responses with shared message history

### `group-chat.py`

Multi-agent (3-agent) conversation system with politician, citizen, and treasury official.

- **Agents**: Politician, Citizen, Treasury Official
- **Rounds**: 6 maximum rounds
- **Mode**: Round-robin agent responses
- **Feature**: Consensus detection when all agents terminate

### `prompt.py`

1. **Agent Initialization**: Three AssistantAgents created with distinct system prompts and OpenAI client
2. **Message Creation**: Initial task message sent to agents as TextMessage object
3. **Agent Response Loop**:
   - Each agent receives all previous messages
   - Agent processes context and generates response via OpenAI API
   - Response appended to shared message history
4. **Conversation Management**: Multiple rounds alternate between agents
5. **Termination**: Conversation ends when max rounds reached or TERMINATE signal detected
6. **Output**: Full message history with all agent contributions

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
