from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model


class TinyKrakenEntry(Model):
    """
    TinyKraken Entry Model class
    """

    class Meta:
        table_name = "tiny-kraken-db"
        region = "eu-west-1"

    pk = UnicodeAttribute(
        hash_key=True, default="hydration_reminder"
    )  # hydration_reminder
    comment_id = UnicodeAttribute(range_key=True)  # UUID
    text = UnicodeAttribute()  # reminder text, AI generated
    created_at = UTCDateTimeAttribute()  # creation timestamp

    def get_comment(self, comment_id: str) -> "TinyKrakenEntry":
        try:
            return self.get(self.pk, comment_id)
        except self.DoesNotExist:
            return None
