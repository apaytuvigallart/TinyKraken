import datetime

import pytest
from hydration_reminder.db import TinyKrakenEntry


@pytest.fixture
def comments():
    return [
        TinyKrakenEntry(
            pk="hydration_reminder",
            comment_id="comment_id_1",
            created_at=datetime.datetime(
                2025, 9, 24, 10, 0, 51, 761516, tzinfo=datetime.timezone.utc
            ),
            text="text 1",
        ),
        TinyKrakenEntry(
            pk="hydration_reminder",
            comment_id="comment_id_2",
            created_at=datetime.datetime(
                2025, 9, 23, 10, 0, 52, 414653, tzinfo=datetime.timezone.utc
            ),
            text="text 2",
        ),
        TinyKrakenEntry(
            pk="hydration_reminder",
            comment_id="comment_id_3",
            created_at=datetime.datetime(
                2025, 9, 22, 13, 54, 51, 296724, tzinfo=datetime.timezone.utc
            ),
            text="text 3",
        ),
    ]


@pytest.fixture
def comment():
    return TinyKrakenEntry(
        pk="hydration_reminder",
        comment_id="comment_id_4",
        created_at=datetime.datetime(
            2025, 9, 24, 10, 0, 51, 761516, tzinfo=datetime.timezone.utc
        ),
        text="text 4",
    )
