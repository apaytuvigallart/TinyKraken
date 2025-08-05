from ai import generate_text
from log import logger
from settings import (
    TO_PHONE_NUMBER,
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_PHONE_NUMBER,
)
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client


def send_notification() -> str:
    """
    This function generates a short, funny sentence reminding someone to drink water and sends it as an SMS message using Twilio.

    Returns:
        str: Confirmation message indicating the text was sent successfully.
    Raises:
        TwilioRestException: If there is an error sending the message.
    """

    if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN:
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
        logger.error("Failed to send notification", extra={"error": str(e)})
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
        logger.error("Lambda function failed", extra={"error": str(e)})
        raise e
