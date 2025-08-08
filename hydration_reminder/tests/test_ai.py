from unittest.mock import Mock, patch

from hydration_reminder.ai import generate_text

MOCKED_AI_TEXT = "Mocked AI generated text"


@patch("hydration_reminder.ai.requests.post")
def test_ai_text_generation(mock_post):
    # Mock GeminiAI response
    mock_response = Mock()
    mock_response.json.return_value = {
        "candidates": [{"content": {"parts": [{"text": MOCKED_AI_TEXT}]}}]
    }
    mock_post.return_value = mock_response

    with (
        patch("hydration_reminder.ai.GOOGLE_API_KEY", "mocked_google_api_key"),
        patch(
            "hydration_reminder.ai.GOOGLE_API_URL",
            "https://mocked.googleapis.com/generateText",
        ),
    ):
        result = generate_text()

        assert result == MOCKED_AI_TEXT
        mock_post.assert_called_once_with(
            "https://mocked.googleapis.com/generateText",
            headers={
                "X-goog-api-key": "mocked_google_api_key",
                "Content-Type": "application/json",
            },
            json={
                "contents": [
                    {
                        "parts": [
                            {
                                "text": "Write a short, funny sentence (15 words or fewer) reminding someone to drink water. It should be playful, clever, and inspired by the Kraken myth or oceanic themes. No emojis."
                            }
                        ]
                    }
                ]
            },
        )
