import random
from collections import UserList


class GetCard(UserList):
    def __init__(self):
        super().__init__()
        self.list = ["Піка", "Чірва", "Буба", "Хреста"]
        self.list1 = ['6', '7', '8', '9', '10', "B", "D", "K", "T"]

    def getnum(self):
        for i in self.list:
            for value in self.list1:
                self.data.append(f"{i} {value}")
        random.shuffle(self.data)
        return random.sample(self.data, k=6)


g = GetCard()

