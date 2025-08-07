import uuid
from datetime import datetime, timezone

from db import TinyKrakenEntry
from log import logger
from pynamodb.exceptions import PutError
from settings import (
    TO_PHONE_NUMBER,
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_PHONE_NUMBER,
)
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client


def save_item(text: str):
    id = str(uuid.uuid4())
    created_at = datetime.now(timezone.utc)

    try:
        item = TinyKrakenEntry(id=id, text=text, created_at=created_at)
        item.save()
        return item

    except PutError as e:
        logger.error("Failed to create item", extra={"error": str(e)})
        raise e


def send_notification(text: str) -> bool:
    """
    This function sends a short, funny SMS reminding someone to drink water.

    Returns:
        bool: True if worked.
    Raises:
        TwilioRestException: If there is an error sending the message.
    """

    if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN:
        raise ValueError("Twilio credentials are not set, dropping ")

    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(to=TO_PHONE_NUMBER, from_=TWILIO_PHONE_NUMBER, body=text)
        logger.info("Message sent successfully", extra={"sentence": text})
        return True

    except TwilioRestException as e:
        logger.error("Failed to send notification", extra={"error": str(e)})
        raise e
