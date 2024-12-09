#provides centralized communication.instead of objects communicating directlywith each otherthey interact through a mediator
class Mediator:
    def send_message(self,message,user):
        pass
class ChatRoom(Mediator):
    def __init__(self,):
        self.users=[]
    def register_user(self,user):
        self.users.append(user)
    def send_message(self,message,sender):
        for user in self.users:
            if user!=sender:
                user.receive_message(message,sender)
class User:
    def __init__(self,name,mediator):
        self.name=name
        self.mediator=mediator
        mediator.register_user(self)
    def send_message(self,message):
        print(f"{self.name}sends:{message}")
        self.mediator.send_message(message,self)
    def receive_message(self,message,sender):
        print(f"{self.name}receives from {sender.name}:{message}")
chat_room=ChatRoom()
alice=User("Alice",chat_room)
arun=User("Arun",chat_room)
arya=User("Arya",chat_room)
alice.send_message("Hello,everyone!")
arun.send_message("Hi alice!")
arya.send_message("hey arun and alice")

