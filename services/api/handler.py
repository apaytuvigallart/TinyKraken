from aws_lambda_powertools.event_handler import APIGatewayRestResolver

app = APIGatewayRestResolver()


@app.get("/comments")
def list_comments() -> dict:
    """
    Get all comments
    """
    print("list_comments")
    return {"message": "list all comments"}


@app.get("/comments/<comment_id>")
def get_comment(comment_id: int) -> dict:
    """
    Get a comment by id
    """
    print("get_comment")
    return {"message": f"get comment {comment_id}"}


def lambda_handler(event, context) -> str:
    """
    Main function to handle the Lambda event and context.
    """
    return app.resolve(event, context)
