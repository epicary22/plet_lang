import json

with open("charsets/shorthand_0b.json", encoding="utf8") as file:
    phon_c = json.load(file)

class PhoneticMessage:

    def __init__(self, msg: str):
        self.msg = msg

    def to_pletlang(self) -> str:
        """
        Turns a PletLang message into its phonetic equivalent.
        """
        msg_copy = self.msg
        phon_msg = ""
        # Shorthand/Longhand
        if msg_copy.startswith("~"):
            form = "shorthand"
        else:
            form = "longhand"
        msg_copy = msg_copy.lstrip("~")
        phon_msg += "/"
        # Message Body
        while not msg_copy.startswith("~"):
            # Convert non-binary chars
            for char in (" ", "."):
                if msg_copy.startswith(char):
                    phon_msg += phon_c[char]
                    msg_copy = msg_copy[1:]
                    continue
            # Convert binary characters
            if form == "shorthand":
                shorthand_slice = msg_copy[:4]
                phon_msg += phon_c[shorthand_slice]
                msg_copy = msg_copy[4:]
            else:
                # !! PLACEHOLDER !!
                longhand_slice = msg_copy[:8]
                phon_msg += phon_c[longhand_slice]
                msg_copy = msg_copy[8:]
        # End Message
        phon_msg += "/"
        return phon_msg
