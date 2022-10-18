import json

with open("charset_translator.json", encoding="utf8") as file:
    charsets = json.load(file)


class CharsetTranslator:

    def __init__(self):
        pass

    def translate_to_binary(self, message, charset_from: str):
        new_message = ""
        if charset_from == "hex":
            for char in message:
                new_message += charsets["hex"][char]
            return new_message
        else:
            print("Charset type not supported.")
            return message
