import json
from charsets.ansi_colors import ANSI_COLORS

BRACKETS = ("1110", "1111")

with open("charsets/shorthand_0b.json", encoding="utf8") as file:
    phon_chars = json.load(file)

with open("charset_translator.json", encoding="utf8") as file:
    charsets = json.load(file)


class PletLangMessage:

    def __init__(self, msg: str) -> None:
        self.msg = msg
        self.pmsg = self.msg  # Pletlang message
        self.format_pmsg()
        self.fmsg = ""  # Fonetic messages

    def format_pmsg(self) -> None:
        self.pmsg = self.pmsg.replace("   ", "TEMP")
        self.pmsg = self.pmsg.replace(" ", "")
        self.pmsg = self.pmsg.replace("TEMP", " ")
        # Charset translator bit

    def get_phonetics(self) -> str:
        if not self.fmsg:
            self.to_phonetics()
        return self.fmsg

    def to_phonetics(self) -> None:
        """
        Turns a PletLang message into its phonetic equivalent.
        """
        def pmsg_delete(num_chars):
            self.pmsg = self.pmsg[num_chars:]

        def brackets_next(text_type: str):
            # TODO somehow fix the brackets system so that it works with 0s and 1s
            pass

        def interpret_brackets():
            if self.pmsg.startswith("{{"):
                self.fmsg += "{*"
                pmsg_delete(2)
                return read_longhand
            elif self.pmsg.startswith("{"):
                self.fmsg += "{"
                pmsg_delete(1)
                return read_shorthand
            elif self.pmsg.startswith("}}"):
                self.fmsg += "*}"
                pmsg_delete(2)
            elif self.pmsg.startswith("}"):
                self.fmsg += "}"
                pmsg_delete(1)
            return "BACK"
            # Return previous message layer type
            # prev_layer = message_layers[-1]
            # if prev_layer == "longhand":
            #     return read_longhand
            # else:
            #     return read_shorthand

        def read_char():
            # Check char's transliteration
            if self.pmsg.startswith((",", "'")):
                self.fmsg += self.pmsg[:1]
                pmsg_delete(1)
            else:
                char_transliteration = self.pmsg[:4]
                self.fmsg += phon_chars[char_transliteration]
                pmsg_delete(4)

        def read_shorthand():
            print("ok")
            while self.pmsg:
                if self.pmsg.startswith(BRACKETS):
                    # Interpret where the message will go next based on brackets
                    next_form = interpret_brackets()
                    if next_form == "BACK":
                        return
                    else:
                        next_form()
                    # Char transliteration
                    read_char()

        def read_longhand():
            print("ok2")
            # Read "{{1101 00000101" as a w in magenta; 0000 is the null color and 1101 is its default.
            default_color = self.pmsg[:4]
            pmsg_delete(4)
            while self.pmsg:
                if self.pmsg.startswith(BRACKETS):
                    # Interpret where the message will go next based on brackets
                    next_form = interpret_brackets()
                    if next_form == "BACK":
                        return
                    else:
                        next_form()
                # Check char's color
                char_color = self.pmsg[:4]
                if char_color == "0000":
                    self.fmsg += ANSI_COLORS[default_color]
                else:
                    self.fmsg += ANSI_COLORS[char_color]
                pmsg_delete(4)
                # Char transliteration
                read_char()
                # Add color ender
                self.fmsg += ANSI_COLORS["END"]

        # Start off by reading the first bracket.
        base_form = interpret_brackets()
        base_form()
