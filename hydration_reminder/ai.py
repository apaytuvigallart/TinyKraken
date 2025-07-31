from google.genai import Client
from settings import GOOGLE_API_KEY


def generate_text() -> str:
    """
    Generate a short, funny sentence reminding someone to drink water
    """
    client = Client(api_key=GOOGLE_API_KEY)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Write a short, funny sentence (15 words or fewer) reminding someone to drink water. It should be playful, clever, and inspired by the Kraken myth or oceanic themes. No emojis.",
    )

    return response.text
