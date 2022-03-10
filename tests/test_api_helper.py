from unittest.mock import MagicMock, patch

from gtd.api_helper import GoogleTranslateAPIHelper

mock_credentials = MagicMock()
mock_credentials.side_effect = ["test credentials"]

mock_translate_client = MagicMock()
mock_translate_client.return_value.translate.side_effect = [{"translatedText": "ok"}]


@patch("google.oauth2.service_account.Credentials.from_service_account_file", mock_credentials)
@patch("google.cloud.translate_v2.Client", mock_translate_client)
def test_translate_text():
    gt = GoogleTranslateAPIHelper()
    assert gt.translate_text("bine", "en") == "ok"
