from unittest.mock import Mock

from hydration_reminder.hydration_reminder.db import TinyKrakenEntry
from hydration_reminder.hydration_reminder.utils import save_item, send_notification


def test_generate_text(monkeypatch):
    # to do
    pass


def test_save_item(monkeypatch):
    # Create mock for save method
    mock_save = Mock()
    monkeypatch.setattr(
        "hydration_reminder.hydration_reminder.utils.TinyKrakenEntry.save", mock_save
    )

    # Test the function
    result = save_item("Drink water!")
    assert isinstance(result, TinyKrakenEntry)
    assert result.text == "Drink water!"


def test_send_notification(monkeypatch):
    # Create mock client instance
    mock_client = Mock()

    # Set up the mock chain properly
    mock_message = Mock()
    mock_client.messages.create.return_value = mock_message

    # Patch all the settings with monkeypatch
    monkeypatch.setattr(
        "hydration_reminder.hydration_reminder.utils.Client",
        Mock(return_value=mock_client),
    )
    monkeypatch.setattr(
        "hydration_reminder.hydration_reminder.utils.TWILIO_ACCOUNT_SID", "test_sid"
    )
    monkeypatch.setattr(
        "hydration_reminder.hydration_reminder.utils.TWILIO_AUTH_TOKEN", "test_token"
    )
    monkeypatch.setattr(
        "hydration_reminder.hydration_reminder.utils.TO_PHONE_NUMBER", "+1234567890"
    )
    monkeypatch.setattr(
        "hydration_reminder.hydration_reminder.utils.TWILIO_PHONE_NUMBER", "+0987654321"
    )

    # Test the function
    result = send_notification("Drink water!")
    assert result is True
