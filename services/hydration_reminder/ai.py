import requests
from log.logger import logger

from hydration_reminder.settings import GOOGLE_API_KEY, GOOGLE_API_URL, PROMPT


def generate_text() -> str:
    """
    Generates a short, funny sentence reminding someone to drink water
    """

    if not GOOGLE_API_KEY or not GOOGLE_API_URL:
        raise ValueError("Google API credentials are not set, dropping")

    prompt = PROMPT
    headers = {"X-goog-api-key": GOOGLE_API_KEY, "Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": prompt}]}]}

    try:
        response = requests.post(GOOGLE_API_URL, headers=headers, json=data)
        response.raise_for_status()

        text = response.json()["candidates"][0]["content"]["parts"][0]["text"]
        logger.info("Text generated successfully", extra={"text": text})

        return text

    except requests.exceptions.RequestException as e:
        logger.error("Failed to generate text", extra={"error": str(e)})
        raise e
