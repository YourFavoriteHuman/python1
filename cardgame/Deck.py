#from Card import Card
import Card
import random
class Deck:
    def __init__(self):
        self.cards = [ ]
        
    def build(self):
        # Append or add 52 cards to deck
        # self.cards.append( Card(2, "Hearts") )
        for suit in Card.Card.SUITS:
            for value in range(2, 15):
                if value == 11:
                    value = "J"
                elif value == 12:
                    value = "Q"
                elif value == 13:
                    value = "K"
                elif value == 14:
                    value = "A"
                self.cards.append((str(value) + suit))
    
    def show(self):
        CARDS_PER_LINE = 13
        cards_printed = 0
        for each_card in self.cards:
            print(each_card, end=" ")
            cards_printed += 1
            
            if cards_printed == CARDS_PER_LINE:
                print()
                cards_printed = 0
                
    def shuffle(self):
        random.shuffle(self.cards)
        return self
    
    def deal(self):
        a_card = self.cards.pop(0)
        return a_card
    
    def deal_many(self, number):
        temp_list = [ ]
        for _ in range(number):
            one_card = self.deal()
            temp_list.append(one_card)
        return temp_list
    
    def return_card(self, one_card):
        self.cards.append(one_card)
        
    def return_many_cards(self, list_of_cards):
        self.cards.extend(list_of_cards)
    