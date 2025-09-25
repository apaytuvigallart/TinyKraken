from http import HTTPStatus

from aws_lambda_powertools.event_handler import Response, content_types
from aws_lambda_powertools.event_handler.exceptions import InternalServerError
from hydration_reminder.hydration_reminder.db import TinyKrakenEntry
from log.logger import logger


class TinyKrakenAPIManager:
    model = TinyKrakenEntry()

    def list_comments(self) -> Response:
        comments = self.model.list_comments()
        if not comments:
            logger.info("No comments found")
            return Response(
                status_code=HTTPStatus.NOT_FOUND,
                content_type=content_types.APPLICATION_JSON,
                body={"message": "No comments found"},
            )

        comments = [
            {
                "comment_id": comment.comment_id,
                "text": comment.text,
                "created_at": str(comment.created_at),
            }
            for comment in comments
        ]
        logger.info("Found comments", extra={"comments": comments})
        try:
            return Response(
                status_code=HTTPStatus.OK,
                content_type=content_types.APPLICATION_JSON,
                body={"comments": comments},
            )
        except InternalServerError as e:
            logger.error(f"Error occurred while listing comments: {e}")
            return Response(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                content_type=content_types.APPLICATION_JSON,
                body={"message": "Internal server error, check logs for details"},
            )

    def get_comment(self, comment_id: str) -> Response:
        comment = self.model.get_comment(comment_id)
        if comment is None:
            logger.info("Comment not found")
            return Response(
                status_code=HTTPStatus.NOT_FOUND,
                content_type=content_types.APPLICATION_JSON,
                body={"message": "Comment not found"},
            )
        logger.info("Found comment", extra={"comment": comment})
        try:
            return Response(
                status_code=HTTPStatus.OK,
                content_type=content_types.APPLICATION_JSON,
                body={
                    "comment_id": comment_id,
                    "text": comment.text,
                    "created_at": str(comment.created_at),
                },
            )
        except InternalServerError as e:
            logger.error(f"Error occurred while getting comment {comment_id}: {e}")
            return Response(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                content_type=content_types.APPLICATION_JSON,
                body={"message": "Internal server error, check logs for details"},
            )
