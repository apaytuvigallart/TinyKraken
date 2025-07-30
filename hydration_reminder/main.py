from ai import generate_text
from settings import ACCOUNT_SID, AUTH_TOKEN
from twilio.rest import Client


def main(receiver: int, sender: int) -> str:
    """
    Main function to send a notification using Twilio.
    """
    if ACCOUNT_SID is None or AUTH_TOKEN is None:
        raise ValueError("Twilio credentials are not set, dropping ")

    sentence = generate_text()
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(to=f"+{receiver}", from_=f"+{sender}", body=sentence)

    return "Message sent successfully: " + sentence


main(
    34123456789, 11234567890
)  # Example phone numbers, include country code, i.e. +34 for Spain
