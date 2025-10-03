import os

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", None)
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", None)
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER", None)
TO_PHONE_NUMBER = os.getenv("TO_PHONE_NUMBER", None)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", None)
GOOGLE_API_URL = os.getenv("GOOGLE_API_URL", None)
PROMPT = "Write a short, funny sentence (15 words or fewer) reminding someone to drink water. It should be playful, clever, and inspired by the Kraken myth or oceanic themes. No emojis. No line break or newline character, such as \\n or <br>."
