from plet_lang_input import PletLangInput
from plet_lang_message import PletLangMessage
import os

os.system("color")

for color in range(30, 37):
    print(f"\x1b[{color}mHello!\x1b[0m")
for color in range(90, 97):
    print(f"\x1b[{color}mHello!\x1b[0m")

print("\x1b[38;2;255;255;0mHello world!\x1b[0m")

if __name__ == "__main__":
    # PletLang message input object
    # Process message with msg.to_phonetics()
    # plet_msg = PletLangInput().__repr__()
    # print(plet_msg.to_phonetics())
    pmsg = PletLangMessage("{ 0100 {{1101 00000101 10101011 }} 1010 }")
    pmsg.to_phonetics()

    # Phonetics message input object
    # Process message with msg.to_plet_lang()
