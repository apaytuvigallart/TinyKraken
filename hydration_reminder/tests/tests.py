from unittest.mock import Mock, patch

from ai import generate_text

MOCKED_AI_TEXT = "Mocked AI generated text"


@patch("ai.Client")
def test_ai_text_generation(mock_client):
    """
    Test AI text generation with mocked response.
    """

    mock_instance = Mock()
    mock_client.return_value = mock_instance

    mock_instance.models.generate_content.return_value.text = MOCKED_AI_TEXT

    result = generate_text()
    print(result)

    assert result == MOCKED_AI_TEXT
