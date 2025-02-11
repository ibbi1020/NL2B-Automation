import os

# Environment variables and configuration
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    raise ValueError("Please set OPENAI_API_KEY environment variable")

BOT_LOCAL = "deepseek-r1:8b"
BOT_REMOTE = "gpt-4o"
OUTPUT_DIR = "./outputs"