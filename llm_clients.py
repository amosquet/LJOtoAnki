from google import genai
from google.genai import types
from mistralai.client import Mistral
from openai import OpenAI

import config


def call_gemini(text_input: str):
    """Sends the text to Google's Gemini model."""
    if not config.GEMINI_API_KEY:
        return "Gemini API key missing."

    client = genai.Client(api_key=config.GEMINI_API_KEY)
    model = "gemini-2.5-flash"
    system = types.GenerateContentConfig(system_instruction=config.SYSTEM_PROMPT)

    # Gemini allows setting the system instruction during model instantiation
    response = client.models.generate_content(
        model=model, contents=text_input, config=system
    )

    # response = model.generate_content(text_input)
    return response.text


def call_chatgpt(text_input: str):
    """Sends the text to OpenAI's ChatGPT (gpt-4o)."""
    if not config.OPENAI_API_KEY:
        return "OpenAI API key missing."

    client = OpenAI(api_key=config.OPENAI_API_KEY)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": config.SYSTEM_PROMPT},
            {"role": "user", "content": text_input},
        ],
    )

    return response.choices[0].message.content


def call_mistral(text_input: str):
    """Sends the text to Mistral's Le Chat API."""
    if not config.MISTRAL_API_KEY:
        return "Mistral API key missing."

    client = Mistral(api_key=config.MISTRAL_API_KEY)
    model = "mistral-large-latest"

    # messages = [
    #     {
    #         "role": "system",
    #         "content": config.SYSTEM_PROMPT,
    #     },
    #     {
    #         "role": "user",
    #         "content": text_input,
    #     },
    # ]

    response = client.chat.complete(
        model=model,
        messages=[
            {"role": "system", "content": config.SYSTEM_PROMPT},
            {"role": "user", "content": text_input},
        ],
    )

    return response.choices[0].message.content


def call_ollama(text_input: str, model_name: str):

    client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama-local")

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": config.SYSTEM_PROMPT},
            {"role": "user", "content": text_input},
        ],
        # temperature = 0.1
    )

    return response.choices[0].message.content
