from Card import Card
from Deck import Deck
d = Deck()
class Pile:
    def __init__(self, name):
        self.name = name
        self.pile_of_cards = [ ]
    
    def add_card_to_pile(self, one_card):
        self.pile_of_cards.append(one_card)
        
    def add_many_to_pile(self, many_cards):
        self.pile_of_cards.extend(many_cards)
        
    def remove_one_card(self):
        a_card = self.pile_of_cards.pop(0)
        return a_card
    
    def get_all_from_pile(self):
        all_cards = self.pile_of_cards.copy()
        self.pile_of_cards.clear()
        return all_cards
        
    def size(self):
        return len(self.pile_of_cards)
    
    def show_pile(self):
        for each_card in self.pile_of_cards:
            print(each_card, end=" ")
        print()