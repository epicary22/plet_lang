from plet_lang_input import PletLangInput
from plet_lang_message import PletLangMessage

if __name__ == "__main__":
    # PletLang message input object
    # Process message with msg.to_phonetics()
    # plet_msg = PletLangInput().__repr__()
    # print(plet_msg.to_phonetics())
    pmsg = PletLangMessage("{ 0100 {{1101 00000101 10101011 }} 1010 }")
    message = pmsg.get_phonetics()

    # Phonetics message input object
    # Process message with msg.to_plet_lang()

print(message)
