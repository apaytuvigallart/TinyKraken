from unittest.mock import Mock

from hydration_reminder.ai import generate_text
from hydration_reminder.db import TinyKrakenEntry
from hydration_reminder.utils import save_item, send_notification

TEXT = "Stay hydrated!"


def test_generate_text(monkeypatch):
    # Create mock for the output of requests.post
    mock_response = Mock()
    mock_response.json.return_value = {
        "candidates": [{"content": {"parts": [{"text": TEXT}]}}]
    }

    # Create mock for requests.post
    mock_post = Mock(return_value=mock_response)

    # Patch requests.post, the API key and URL
    monkeypatch.setattr("hydration_reminder.ai.requests.post", mock_post)
    monkeypatch.setattr("hydration_reminder.ai.GOOGLE_API_KEY", "test_key")
    monkeypatch.setattr("hydration_reminder.ai.GOOGLE_API_URL", "https://test.url")

    # Test the function
    result = generate_text()
    assert result == TEXT
    assert mock_post.call_args[0][0] == "https://test.url"
    mock_post.assert_called_once()


def test_save_item(monkeypatch):
    # Create mock for save method
    mock_save = Mock()
    monkeypatch.setattr("hydration_reminder.utils.TinyKrakenEntry.save", mock_save)

    # Test the function
    result = save_item(TEXT)
    assert isinstance(result, TinyKrakenEntry)
    assert result.text == TEXT


def test_send_notification(monkeypatch):
    # Create mock client instance
    mock_client = Mock()

    # Set up the mock chain properly
    mock_message = Mock()
    mock_client.messages.create.return_value = mock_message

    # Patch all the settings with monkeypatch
    monkeypatch.setattr(
        "hydration_reminder.utils.Client",
        Mock(return_value=mock_client),
    )
    monkeypatch.setattr("hydration_reminder.utils.TWILIO_ACCOUNT_SID", "test_sid")
    monkeypatch.setattr("hydration_reminder.utils.TWILIO_AUTH_TOKEN", "test_token")
    monkeypatch.setattr("hydration_reminder.utils.TO_PHONE_NUMBER", "+1234567890")
    monkeypatch.setattr("hydration_reminder.utils.TWILIO_PHONE_NUMBER", "+0987654321")

    # Test the function
    result = send_notification(TEXT)
    assert result is True
