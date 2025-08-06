from unittest.mock import Mock, patch

from ai import generate_text
from lambda_function import send_notification

MOCKED_AI_TEXT = "Mocked AI generated text"


@patch("ai.requests.post")
def test_ai_text_generation(mock_post):
    # Mock GeminiAI response
    mock_response = Mock()
    mock_response.json.return_value = {
        "candidates": [{"content": {"parts": [{"text": MOCKED_AI_TEXT}]}}]
    }
    mock_post.return_value = mock_response

    with (
        patch("ai.GOOGLE_API_KEY", "mocked_google_api_key"),
        patch("ai.GOOGLE_API_URL", "https://mocked.googleapis.com/generateText"),
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


@patch("lambda_function.Client")
@patch("lambda_function.generate_text")
def test_send_notification(mocked_text, mocked_twilio_client):
    # Mock text
    mocked_text.return_value = MOCKED_AI_TEXT

    # Mock Twilio client instance and message
    mocked_client_instance = Mock()
    mocked_message = Mock()
    mocked_client_instance.messages.create.return_value = mocked_message

    # Assign the mock instance as the return value of the Client constructor
    mocked_twilio_client.return_value = mocked_client_instance

    with (
        patch("lambda_function.TWILIO_ACCOUNT_SID", "mocked_twilio_account_sid"),
        patch("lambda_function.TWILIO_AUTH_TOKEN", "mocked_twilio_auth_token"),
        patch("lambda_function.TO_PHONE_NUMBER", "+1234567890"),
        patch("lambda_function.TWILIO_PHONE_NUMBER", "+0987654321"),
    ):
        result = send_notification()
        assert result == f"Message sent successfully: {MOCKED_AI_TEXT}"
        mocked_twilio_client.assert_called_once()
        mocked_client_instance.messages.create.assert_called_once_with(
            to="+1234567890", from_="+0987654321", body=MOCKED_AI_TEXT
        )
