from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model


class TinyKrakenEntry(Model):
    """
    TinyKraken Entry Model class
    """

    class Meta:
        table_name = "tiny-kraken-db"
        region = "eu-west-1"

    id = UnicodeAttribute(hash_key=True)
    text = UnicodeAttribute()
    created_at = UTCDateTimeAttribute()
