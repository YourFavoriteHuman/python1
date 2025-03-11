from Card import Card
from Deck import Deck
class Pile:
    def __init__(self, name):
        self.name = name
        self.cards = [ ]
    
    def add_card(self, one_card):
        self.cards.append(one_card)
        
    def remove_all(self):
        self.cards.clear()
    
    def show(self):
        for each_card in self.cards:
            print(each_card, "-", each_card.color, end=" ")
        print()

p = Pile("play1")
d = Deck()
p.show()