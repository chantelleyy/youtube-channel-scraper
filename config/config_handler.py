import os
from dotenv import load_dotenv

def load_api_key():
    load_dotenv()
    api_key = os.getenv("YOUTUBE_API_KEY")
    if not api_key:
        raise ValueError("Missing API key in .env file.")
    return api_key