import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_llm_reply(user_text, recommendations):
    catalog_text = ""

    for item in recommendations:
        catalog_text += f"Name: {item['name']}\n"
        catalog_text += f"Type: {item['test_type']}\n"
        catalog_text += f"Description: {item['description']}\n"
        catalog_text += f"URL: {item['url']}\n\n"

    prompt = f"""
You are an SHL assessment recommendation assistant.

User requirement:
{user_text}

Recommended catalog items:
{catalog_text}

Write a short helpful reply explaining why these assessments fit.
Do not invent assessments.
Do not include any URL that is not listed above.
Keep the answer concise.
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception:
        return f"Here are {len(recommendations)} SHL assessments that match your requirement."