from langchain_groq import ChatGroq
from config.config import GROQ_API_KEY


def load_llm():
    try:
        llm = ChatGroq(
            api_key=GROQ_API_KEY,
            model="llama-3.1-8b-instant",
            temperature=0.3
        )
        return llm

    except Exception as e:
        print(f"Error loading LLM: {e}")
        return None