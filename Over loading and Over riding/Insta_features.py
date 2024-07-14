class Insta_features():

    def __init__(self, name, username, *args, **kwargs):
        self.name = name
        self.username = username
        self.args = args
        self.kwargs = kwargs

    def chat(self, sender: int, receiver: int, text: str):
        pass

    def audio(self, sender: int, receiver: int, audio):
        pass

    def video(self, sender: int, receiver: int, video: bool):
        pass

    def send_reel(self, sender: int, receiver: int, photo):
        pass
