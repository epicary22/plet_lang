class MessageInput:

    def __init__(self):
        self.start_msg: str
        self.repeat_msg: str
        self.msg = input(self.start_msg)
        while not self.scan():
            self.msg = input(self.repeat_msg)

    def scan(self) -> bool:
        pass 

