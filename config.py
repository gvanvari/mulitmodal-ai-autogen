import os

from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

config_list_openai = [
    {
        "model": "gpt-4o-mini",
        "api_key": openai_api_key,
    }
]

llm_config_openai = {
    "config_list": config_list_openai,
    "timeout": 120,
}
