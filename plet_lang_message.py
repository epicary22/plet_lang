import json
from charsets.ansi_colors import ANSI_COLORS

BRACKETS = ("{", "}")

with open("charsets/shorthand_0b.json", encoding="utf8") as file:
    phon_chars = json.load(file)

class PletLangMessage:

    def __init__(self, msg: str):
        self.msg = msg
        self.__pmsg = self.msg  # Pletlang message
        self.__pmsg = self.__pmsg.replace("   ", "TEMP")
        self.__pmsg = self.__pmsg.replace(" ", "")
        self.__pmsg = self.__pmsg.replace("TEMP", " ")
        print(self.__pmsg)
        self.__message_layers = []
        self.fmsg = ""  # Fonetic message

    def to_phonetics(self) -> str:
        """
        Turns a PletLang message into its phonetic equivalent.
        """
        def pmsg_delete(num_chars):
            self.__pmsg = self.__pmsg[num_chars:]

        def interpret_brackets():
            global message_layers
            if self.__pmsg.startswith("{{"):
                self.fmsg += "{*"
                pmsg_delete(2)
                self.__message_layers.append("longhand")
                return read_longhand
            elif self.__pmsg.startswith("{"):
                self.fmsg += "{"
                pmsg_delete(1)
                self.__message_layers.append("shorthand")
                return read_shorthand
            elif self.__pmsg.startswith("}}"):
                self.fmsg += "*}"
                pmsg_delete(2)
                self.__message_layers.pop(-1)
            elif self.__pmsg.startswith("}"):
                self.fmsg += "}"
                pmsg_delete(1)
                self.__message_layers.pop(-1)
            return "BACK"
            # Return previous message layer type
            # prev_layer = message_layers[-1]
            # if prev_layer == "longhand":
            #     return read_longhand
            # else:
            #     return read_shorthand

        def read_shorthand():
            next_form = None
            print("e")

            while self.__pmsg:
                if self.__pmsg.startswith(BRACKETS):
                    # Interpret where the message will go next based on brackets
                    next_form = interpret_brackets()
                    if next_form == "BACK":
                        return
                    else:
                        next_form()
                # Check char's transliteration
                elif self.__pmsg.startswith((",", "'")):
                    self.fmsg += self.__pmsg[:1]
                    pmsg_delete(1)
                else:
                    char_transliteration = self.__pmsg[:4]
                    self.fmsg += phon_chars[char_transliteration]
                    pmsg_delete(4)

        def read_longhand():
            # Read "{{1101 00000101" as a w in magenta; 0000 is the null color and 1101 is its default.
            default_color = self.__pmsg[:4]
            pmsg_delete(4)
            while self.__pmsg:
                if self.__pmsg.startswith(BRACKETS):
                    # Interpret where the message will go next based on brackets
                    next_form = interpret_brackets()
                    if next_form == "BACK":
                        return
                    else:
                        next_form()
                # Check char's color
                char_color = self.__pmsg[:4]
                if char_color == "0000":
                    self.fmsg += ANSI_COLORS[default_color]
                else:
                    self.fmsg += ANSI_COLORS[char_color]
                pmsg_delete(4)
                # Check char's transliteration
                if self.__pmsg.startswith((",", "'")):
                    self.fmsg += self.__pmsg[:1]
                    pmsg_delete(1)
                else:
                    char_transliteration = self.__pmsg[:4]
                    self.fmsg += phon_chars[char_transliteration]
                    pmsg_delete(4)
                # Add color ender
                self.fmsg += ANSI_COLORS["END"]

        # Start off by reading the first bracket.
        base_form = interpret_brackets()
        base_form()
        return self.fmsg

p = PletLangMessage("{ 0100 {{1011 00000101 11001001 0110' }} 0000 }")
print(p.to_phonetics())
