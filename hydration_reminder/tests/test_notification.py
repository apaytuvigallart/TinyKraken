from unittest.mock import Mock, patch

from hydration_reminder.utils import send_notification

MOCKED_AI_TEXT = "Mocked AI generated text"


@patch("hydration_reminder.utils.Client")
def test_send_notification(mocked_twilio_client):
    # Mock Twilio client instance and message
    mocked_client_instance = Mock()
    mocked_message = Mock()
    mocked_client_instance.messages.create.return_value = mocked_message

    # Assign the mock instance as the return value of the Client constructor
    mocked_twilio_client.return_value = mocked_client_instance

    with (
        patch(
            "hydration_reminder.utils.TWILIO_ACCOUNT_SID", "mocked_twilio_account_sid"
        ),
        patch("hydration_reminder.utils.TWILIO_AUTH_TOKEN", "mocked_twilio_auth_token"),
        patch("hydration_reminder.utils.TO_PHONE_NUMBER", "+1234567890"),
        patch("hydration_reminder.utils.TWILIO_PHONE_NUMBER", "+0987654321"),
    ):
        result = send_notification(MOCKED_AI_TEXT)
        assert result is True
        mocked_twilio_client.assert_called_once()
        mocked_client_instance.messages.create.assert_called_once_with(
            to="+1234567890", from_="+0987654321", body=MOCKED_AI_TEXT
        )
