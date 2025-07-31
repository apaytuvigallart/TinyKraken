from unittest.mock import Mock, patch

from ai import generate_text
from main import main

MOCKED_AI_TEXT = "Mocked AI generated text"
MOCKED_TO = "+1234567890"
MOCKED_FROM = "+0987654321"


@patch("main.Client")
@patch("main.generate_text")
def test_notification(mock_generate_text, mock_client):
    """
    Test sending a notification using Twilio with mocked AI text generation.
    """
    mock_instance = Mock()
    mock_client.return_value = mock_instance

    mock_instance.messages = Mock()

    mock_generate_text.return_value = MOCKED_AI_TEXT

    result = main(MOCKED_TO, MOCKED_FROM)

    assert result == f"Message sent successfully: {MOCKED_AI_TEXT}"
    mock_instance.messages.create.assert_called_with(
        to=MOCKED_TO, from_=MOCKED_FROM, body=MOCKED_AI_TEXT
    )


@patch("ai.Client")
def test_ai_text_generation(mock_client):
    """
    Test AI text generation with mocked response."""
    mock_instance = Mock()
    mock_client.return_value = mock_instance

    mock_instance.models.generate_content.return_value.text = MOCKED_AI_TEXT

    result = generate_text()

    assert result == MOCKED_AI_TEXT
