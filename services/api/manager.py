from hydration_reminder.db import TinyKrakenEntry


class TinyKrakenAPIManager:
    def list_comments(self):
        pass

    def get_comment(self, comment_id: str):
        model = TinyKrakenEntry()
        comment = model.get_comment(comment_id)
        if comment is None:
            return {}

        return {
            "comment_id": comment_id,
            "text": comment.text,
            "created_at": str(comment.created_at),
        }
