def print_markdown(text):
    display(Markdown(text))


def print_chat_history(chat_result):
    """Any chat result object has a chat_history attribute that contains the conversation history.
    This function prints the conversation history in a readable format.
    """
    for i in chat_result.chat_history:
        print_markdown(i["name"])
        print("_" * 100)
        print_markdown(i["content"])
        print("_" * 100)
