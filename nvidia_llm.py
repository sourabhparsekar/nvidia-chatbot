from langchain_nvidia_ai_endpoints import ChatNVIDIA
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()

LLM_KEY = os.getenv("NVIDIA_KEY")

# Create NVIDIA chat client
llm = ChatNVIDIA(
    model="deepseek-ai/deepseek-r1",
    api_key=LLM_KEY,
    temperature=0.6,
    top_p=0.7,
    max_tokens=4096,
)
