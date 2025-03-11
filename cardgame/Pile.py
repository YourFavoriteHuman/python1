class Pile:
    def __init__(self, name):
        self.name = name
        self.cards = [ ]
    
    def add_card(self, one_card):
        self.cards.append(one_card)
        
    def remove_all(self):
        self.cards.clear()