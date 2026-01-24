# backend/core/llm.py

from langchain_google_genai import ChatGoogleGenerativeAI


def get_gemini_model(api_key: str):
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        google_api_key=api_key,
        temperature=0.5,
        max_output_tokens=1000,
        timeout=10,
    )
