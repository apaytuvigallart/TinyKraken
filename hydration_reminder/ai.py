import requests
from settings import GOOGLE_API_KEY, GOOGLE_API_URL


def generate_text() -> str:
    """
    Generate a short, funny sentence reminding someone to drink water
    """

    prompt = "Write a short, funny sentence (15 words or fewer) reminding someone to drink water. It should be playful, clever, and inspired by the Kraken myth or oceanic themes. No emojis."
    url = GOOGLE_API_URL
    headers = {"X-goog-api-key": GOOGLE_API_KEY, "Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    response = requests.post(url, headers=headers, json=data)

    return response.json()["candidates"][0]["content"]["parts"][0]["text"]
