import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


def summarize_text(text):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY not found.")

    client = genai.Client(api_key=api_key)

    prompt = f"""
Summarize the following content.

Requirements:
- Maximum 150 words.
- Keep only the key information.
- Do not invent facts.
- If information is insufficient, clearly state that.

Content:
{text}
"""

    response = client.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=prompt,
    )

    return response.text