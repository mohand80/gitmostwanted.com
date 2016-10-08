import re
import unicodedata


class TextWithoutSmilies:
    pattern = '\s*:[a-z0-9_-]+:\s*'

    def __init__(self, text: str):
        self.__text = unicodedata.normalize('NFC', text)

    def __str__(self):
        return re.sub(self.pattern, ' ', self.__text).strip()
