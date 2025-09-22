from hydration_reminder.db import TinyKrakenEntry


class TinyKrakenAPIManager:
    model = TinyKrakenEntry()

    def list_comments(self):
        comments = self.model.list_comments()
        return [
            {
                "comment_id": comment.comment_id,
                "text": comment.text,
                "created_at": str(comment.created_at),
            }
            for comment in comments
        ]

    def get_comment(self, comment_id: str):
        comment = self.model.get_comment(comment_id)
        if comment is None:
            return {}

        return {
            "comment_id": comment_id,
            "text": comment.text,
            "created_at": str(comment.created_at),
        }
