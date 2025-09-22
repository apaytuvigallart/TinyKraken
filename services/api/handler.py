from aws_lambda_powertools.event_handler import APIGatewayRestResolver

from api.manager import TinyKrakenAPIManager

app = APIGatewayRestResolver()
api_manager = TinyKrakenAPIManager()


@app.get("/comments")
def list_comments() -> dict:
    """
    Get all comments
    """
    return api_manager.list_comments()


@app.get("/comments/<comment_id>")
def get_comment(comment_id: str) -> dict:
    """
    Get a comment by id
    """
    return api_manager.get_comment(comment_id)


def lambda_handler(event, context) -> str:
    """
    Main function to handle the Lambda event and context.
    """
    return app.resolve(event, context)
