from ai import generate_text
from log import logger
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client

from settings import (
    TO_PHONE_NUMBER,
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_PHONE_NUMBER,
)


def send_notification() -> str:
    """
    Send a notification using Twilio with a generated text.
    """

    if TWILIO_ACCOUNT_SID is None or TWILIO_AUTH_TOKEN is None:
        raise ValueError("Twilio credentials are not set, dropping ")

    try:
        sentence = generate_text()
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(
            to=TO_PHONE_NUMBER, from_=TWILIO_PHONE_NUMBER, body=sentence
        )
        logger.info("Message sent successfully", extra={"sentence": sentence})
        return "Message sent successfully: " + sentence

    except TwilioRestException as e:
        raise e


def lambda_handler(event, context) -> str:
    """
    Main function to handle the Lambda event and context.
    """

    logger.info("Lambda function started", extra={"event": event})

    try:
        result = send_notification()
        logger.info("Lambda function completed successfully")
        return result

    except Exception as e:
        raise e
