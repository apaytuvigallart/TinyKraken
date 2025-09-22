from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.indexes import AllProjection, GlobalSecondaryIndex
from pynamodb.models import Model
from pynamodb.pagination import ResultIterator


class TinyKrakenGlobalSecondaryIndex(GlobalSecondaryIndex):
    class Meta:
        index_name = "TinyKrakenGlobalSecondaryIndex"
        projection = AllProjection()
        read_capacity_units = 5
        write_capacity_units = 5

        pk = UnicodeAttribute(hash_key=True, default="hydration_reminder")
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
    sk = UnicodeAttribute(range_key=True)  # UUID
    text = UnicodeAttribute()  # reminder text, AI generated
    created_at = UTCDateTimeAttribute()  # creation timestamp

    global_sort_key_index = TinyKrakenGlobalSecondaryIndex()

    @classmethod
    def list_comments(cls) -> ResultIterator["TinyKrakenEntry"]:
        """
        List the newest 10 comments
        """

        return TinyKrakenEntry.global_sort_key_index.query(
            "hydration_reminder", scan_index_forward=False, limit=10
        )

    @classmethod
    def get_comment(cls, sk: str) -> "TinyKrakenEntry":
        """
        Get a comment by its sk
        """

        return TinyKrakenEntry.get("hydration_reminder", sk)
