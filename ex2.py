import random

from ex1 import GetCard

g = GetCard()
gamers = ["Sasha", "Alina", "Masha", "Misha"]


class GetCardsForUsers:
    def __init__(self, gamers: list, g: GetCard) -> None:
        self.dict = {}
        self.gamers = gamers
        self.g = g
        self.limit_line = 6

    def get_users(self) -> dict:
        for i in self.gamers:
            self.dict.update({i: self.g.getnum()})
        print(self.dict)
        return self.dict

    def __str__(self):
        view = ''
        string = str(random.sample(g.data, k=1)) + ' -> Козирка'
        view = view + "{:^160}".format(string) + "\n"
        view = view.replace('[', "")
        view = view.replace(']', "")
        view = view + '{:^40}{:^40}{:^40}{:^40}'.format(*self.dict) + '\n'
        for i in range(self.limit_line):
            line = []
            for k in self.dict:
                line.append(self.dict[k][i])
            view = view + '{:^40}{:^40}{:^40}{:^40}'.format(*line) + '\n'
        return view


c = GetCardsForUsers(gamers, g)
c.get_users()
print(c)




