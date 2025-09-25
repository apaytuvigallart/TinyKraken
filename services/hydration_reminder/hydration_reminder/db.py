from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.indexes import AllProjection, GlobalSecondaryIndex
from pynamodb.models import Model


class TinyKrakenEntryGlobalSecondaryIndex(GlobalSecondaryIndex):
    """
    TinyKrakenEntry Global Secondary Index
    """

    class Meta:
        index_name = "TinyKrakenEntryIndex"
        projection = AllProjection()
        read_capacity_units = 5
        write_capacity_units = 5

    pk = UnicodeAttribute(hash_key=True)
    created_at = UTCDateTimeAttribute(range_key=True)


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

    global_secondary_index = TinyKrakenEntryGlobalSecondaryIndex()

    def get_comment(self, comment_id: str) -> "TinyKrakenEntry":
        try:
            return self.get(self.pk, comment_id)
        except self.DoesNotExist:
            return None

    def list_comments(self) -> list["TinyKrakenEntry"]:
        comments = self.global_secondary_index.query(
            self.pk, limit=10, scan_index_forward=False
        )
        return list(comments)
