class Deck:
    # Class variables
    SUITS = ["♤", "♡", "♧", "♢"]
    NAMES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    
    # Constructor
    def __init__(self, suit, value):
        # Instance variables
        self.suit = suit        # Ex: "Hearts"
        self.value = value      # Ex: 2...10, 11, 12, 13, 14
        if self.suit == "Heart" or self.suit == "Diamonds":
            self.color = "red"
        else:
            self.color = "black"
        
    def __str__(self):
        # Output this: 4♡ K♧ 10♢
        s = Deck.NAMES[self.value][0]

    def build(self):
        for suit in Deck.SUITS:
            pass