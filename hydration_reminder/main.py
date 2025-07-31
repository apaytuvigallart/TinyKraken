from ai import generate_text
from settings import (
    TO_PHONE,
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_PHONE_NUMBER,
)
from twilio.rest import Client


def main(receiver: str, sender: str) -> str:
    """
    Main function to send a notification using Twilio.
    """
    if TWILIO_ACCOUNT_SID is None or TWILIO_AUTH_TOKEN is None:
        raise ValueError("Twilio credentials are not set, dropping ")
    try:
        sentence = generate_text()
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(to=receiver, from_=sender, body=sentence)

        return "Message sent successfully: " + sentence

    except Exception as e:
        return "Failed to send message: " + str(e)


main(receiver=TO_PHONE, sender=TWILIO_PHONE_NUMBER)
