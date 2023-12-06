from enum import Enum

class Models(Enum):
    GPT3 = "gpt-3.5-turbo"
    GPT4 = "gpt-4"

class Roles(Enum):
    SYSTEM = "system"
    ASSISTANT = "assistant"
    USER = "user"

API_KEY_PATH = "api_key.txt"
