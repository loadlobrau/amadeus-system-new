from dotenv import load_dotenv
import os

load_dotenv()

LLM_API_KEY = os.getenv("LLM_API_KEY")
WHISPER_API_KEY = os.getenv("WHISPER_API_KEY")
SILICONFLOW_API_KEY = os.getenv("SILICONFLOW_API_KEY")
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "https://api.ephone.ai/v1")
WHISPER_BASE_URL = os.getenv("WHISPER_BASE_URL", "https://amadeus-ai-api-2.zeabur.app/v1")
STUN_URLS = os.getenv("STUN_URLS", "")
TURN_URLS = os.getenv("TURN_URLS", "")
TURN_USERNAME = os.getenv("TURN_USERNAME", "")
TURN_CREDENTIAL = os.getenv("TURN_CREDENTIAL", "")
