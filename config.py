import os

from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY", "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")

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "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")