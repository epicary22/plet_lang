from message_input import MessageInput
from plet_lang_message import PletLangMessage


class PletLangInput(MessageInput):

    def __init__(self):
        self.start_msg = "Input a PletLang message:\n"
        self.repeat_msg = "Please try again:\n"
        super().__init__()

    def __repr__(self):
        return PletLangMessage(self.msg)

    def scan(self) -> bool:
        """
        Bare minimum for a PletLang message:
        ~(~)MESSAGE~    
        """
        errors = []
        split_msg = list(self.msg)
        # Check ~
        if self.msg.startswith("~"):
            if (split_msg.count("0") + split_msg.count("1")) % 4 != 0:
                errors.append("The number of bits in a shorthand message must be a multiple of 4!")
            if self.msg.endswith("~~"):
                errors.append("Only use '~' at the end of a message!")
            elif self.msg.endswith("~") and split_msg.count("~") > 2:
                errors.append("Only use '~'s to start and end the message!")
        # Check ~~
        elif self.msg.startswith("~~"):
            if (split_msg.count("0") + split_msg.count("1")) % 8 != 0:
                errors.append("The number of bits in a longhand message must be a multiple of 8!")
            if self.msg.endswith("~~"):
                errors.append("Only use '~' at the end of a message!")
            elif self.msg.endswith("~") and split_msg.count("~") > 3:
                errors.append("Only use '~'s to start and end the message!")
        else:
            errors.append("Use '~' or '~~' at the start of the message!")
        # Check ending ~
        if not self.msg.endswith("~"):
            errors.append("Put '~' at the end of the message!")
        if errors:
            for error in errors:
                print(error)
            return False
        return True

