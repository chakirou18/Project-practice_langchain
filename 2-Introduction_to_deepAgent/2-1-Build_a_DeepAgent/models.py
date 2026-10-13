import os  # noqa: F401  # used in commented-out model examples below
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env", override=True)

from langchain.chat_models import init_chat_model
model = init_chat_model("openai:gpt-4.1-mini")
