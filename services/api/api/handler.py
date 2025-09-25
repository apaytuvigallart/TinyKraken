from aws_lambda_powertools.event_handler import APIGatewayRestResolver, Response
from log.logger import logger

from .manager import TinyKrakenAPIManager

app = APIGatewayRestResolver()
api_manager = TinyKrakenAPIManager()


@app.get("/comments")
def list_comments() -> Response:
    """
    Get all comments
    """
    logger.info("API request /comments")
    return api_manager.list_comments()


@app.get("/comments/<comment_id>")
def get_comment(comment_id: str) -> Response:
    """
    Get a comment by id
    """
    logger.info("API request /comments/<comment_id>", extra={"comment_id": comment_id})
    return api_manager.get_comment(comment_id)


def lambda_handler(event, context):
    """
    Main function to handle the Lambda event and context.
    """

    logger.info("Lambda function initialized", extra={"event": event})
    return app.resolve(event, context)
