import Deck

class Card(Deck):
        # Class variables
    SUITS = ["♤", "♡", "♧", "♢"]
    SUITS2 = ["Spades", "Hearts", "Clubs", "Diamonds"]
    NAMES = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    
    
    # Constructor
    def __init__(self, suit, value):
        # Instance variables
        self.suit = suit.title()     # Ex: "Hearts"
        self.value = value      # Ex: 2...10, 11, 12, 13, 14
        
        if self.suit == "Heart" or self.suit == "Diamonds":
            self.color = "red"
        else:
            self.color = "black"
        
        self.long_name = Deck.NAMES[self.value] + " of " + self.suit
        
        if self.value == 10:
            self.name = Card.NAMES[self.value][:2] + Card.SUITS[Card.SUITS2.index[self.suit]]
        else:
            self.name = Card.NAMES[self.value][0] + Card.SUITS[Card.SUITS2.index[self.suit]]
            
        self.back_image = "card_back_red.png"
        self.front_image = self.long_name.replace(" ", "_").lower() + ".png"
    def __str__(self):
        # Output this: 4♡ K♧ 10♢
        s = Deck.NAMES[self.value][0]

    def build(self):
        for suit in Deck.SUITS:
            pass
    
