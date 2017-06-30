from datetime import datetime
#_____this is spy class____
class Spy:
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

class ChatMessage:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('ak', 'Mr.', 24, 4.7)
#----friends list-------

friend_one = Spy('UJWAL', 'Mr.', 27, 4.9)
friend_two = Spy('vk', 'Ms.', 21, 4.39)
friend_three = Spy('PIYUSH', 'Dr.', 37, 4.95)

friends = [friend_one, friend_two, friend_three]

class maintain:
    count =1
    get = 0

    def __init__(self,text,):
        self.txt =text
        maintain.get =( maintain.get + len(self.txt.split()))
        maintain.count += 1
