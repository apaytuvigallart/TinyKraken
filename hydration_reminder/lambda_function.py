from ai import generate_text
from log import logger
from utils import save_item, send_notification


def lambda_handler(event, context) -> str:
    """
    Main function to handle the Lambda event and context.
    """

    logger.info("Lambda function started", extra={"event": event})

    try:
        text = generate_text()
        send_notification(text)
        save_item(text)

        logger.info("Lambda function completed successfully")
        return "Lambda function completed successfully"

    except Exception as e:
        logger.error("Lambda function failed", extra={"error": str(e)})
        raise e
