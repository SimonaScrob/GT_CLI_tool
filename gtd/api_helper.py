import six

from google.cloud import translate_v2 as translate
from google.oauth2 import service_account
from settings import SERVICE_ACCOUNT_KEY_PATH


class GoogleTranslateAPIHelper:
    def __init__(self):
        self.__credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_KEY_PATH)
        self.__translate_client = translate.Client(credentials=self.__credentials)

    def translate_text(self, target, text):
        """Translates text into the target language.
        Target must be an ISO 639-1 language code.
        See https://g.co/cloud/translate/v2/translate-reference#supported_languages
        """
        if isinstance(text, six.binary_type):
            text = text.decode("utf-8")

        result = self.__translate_client.translate(text, target_language=target)
        return result["translatedText"]
