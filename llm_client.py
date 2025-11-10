import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def get_summary(text, max_tokens=180):
    prompt = "Provide a plain-English summary (TL;DR) of the following webpage text:\n\n" + text[:4000]
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()

def get_simplified(text, max_tokens=180):
    prompt = "Rewrite the following webpage text for better readability, in simple language for a general audience:\n\n" + text[:4000]
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()
