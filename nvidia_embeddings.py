from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

LLM_KEY = os.getenv("NVIDIA_KEY")

nvidia_embeddings = NVIDIAEmbeddings(
    model="nvidia/nv-embedqa-e5-v5",
    api_key=LLM_KEY,
    truncate="NONE",
)
