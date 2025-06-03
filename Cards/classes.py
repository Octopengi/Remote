#Components pls 
import random
import functions as Func

class GameMaster:
    def __init__(self):
        self.suites = ["Diamond", "Heart", "Spade", "Club"]
        self.ranks = ["1", "2", "3", "4", "5", "6", "7", "8"]

    """def Distribute(self):
        suite = random.choices(self.suites)
        rank = random.choices(self.ranks)
        return Card(suite[0], rank[0])"""

class Card:
    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank
        self.name = suite + " " + rank

class Hand:
    def __init__(self):
        self.hand = []
        self.turn = True

    def Draw(self, quant):
        for i in range(0, quant):
            self.hand.append(Func.Distribute())

    def PlayCard(self, listNum, display = False):
        if display:
            print("Played a " + self.hand[listNum - 1].name + "!")
        return self.hand.pop(listNum - 1)

    def ShowHand(self, form):
        form = form.lower()
        if len(self.hand) == 0:
            print("This hand is empty!")
        else:
            for i in range(0, len(self.hand)):
                if form == "line":
                    print(self.hand[i].name + " |", end=" ") 
                elif form == "list":
                    print(str(i + 1) + " = " + self.hand[i].name)