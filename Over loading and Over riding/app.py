from Insta_features import Insta_features


class Insta(Insta_features):
    def chat(self, sender: str, receiver: str, text: str):
        return f'*From "{self.name}" to username = {sender}, You Got Message = {text}'

    def send_reel(self, sender: str, receiver: str, reel: bool) -> dict:
        print(f'*From "{sender}" to username = {receiver}, Sent reel= {reel}')
        return {"status": reel}

    def audio(self, sender: str, receiver: str, audio):
        print(f'*From "{sender}" to username = {receiver}, Audio Sent = {audio}')
        return {"Audio status": audio}

    def video(self, sender: str, receiver: str, video: bool):
        print(f'*From "{sender}" to username= {receiver}, Video Call = {video}')
        return {"Video status": video}


print("Person1 Insta status:-\n")
person1 = Insta(name="dinesh", username = "dinesh@23")
print(person1.chat(sender= "dinesh", receiver="john_345", text="Hi,How are You?"))
print(person1.send_reel(sender= "dinesh", receiver="don_#123", reel=True))
print(person1.audio(sender= "dinesh", receiver="Lee@234", audio=True))
print("*******************************************************************")
print("Person2 Insta status:-\n")
person2 = Insta(name="King Kong", username = "konh@1970")
print(person2.chat(sender="Kong", receiver="king$34", text="I'm KingKong, Who are you?"))
print(person2.send_reel(sender="Kong", receiver="don_#123", reel=True))
print(person2.audio(sender="Kong", receiver="Lee@234", audio=False))
print(person2.video(sender="Kong",receiver="Gor@#$",video=True))
