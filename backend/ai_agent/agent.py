import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from ai_agent.graph import graph

# Load .env from backend folder
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

llm = ChatGroq(
    model="gemma2-9b-it",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0,
)


def ask_ai(user_input: str):
    result = graph.invoke(
        {
            "user_input": user_input,
            "response": "",
        }
    )

    return result["response"]