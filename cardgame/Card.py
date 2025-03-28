class Card:
    # Class Variables
    SUITS = ["♤", "♡", "♧", "♢"]
    SUITS2 = ["Clubs", "Diamonds", "Hearts", "Spades"]
    NAMES = [None, None, "2", "3", "4", "5", "6", "7",
    "8", "9", "10","Jack", "Queen", "King", "Ace"]
    GUI_SCALE_FACTOR = 0.3
    

    # Constructor
    def __init__(self, value, suit):
        
        # Instance Variables
        self.suit = suit.title() # Ex: "Hearts"
        self.value = value # Ex: 2...10, 11, 12, 13, 14
        self = self

        if self.suit == "Hearts" or self.suit == "Diamonds":
            self.color = "Red"
        else:
            self.color = "Black"

        self.long_name = Card.NAMES[self.value] + " of " + self.suit

        if self.value == 10:
            self.name = Card.NAMES[self.value][:2] + Card.SUITS[ Card.SUITS2.index(self.suit)]
        else:
            self.name = Card.NAMES[self.value][0] + Card.SUITS[ Card.SUITS2.index(self.suit)]

        self.back_image = "back.png"

        """
        # Temp variables
        front_image = self.long_name.replace(" ", "_").lower() + ".png"
        im = Image.open(f"images/{front_image}")
        image = im.resize((round(im.size[0]*Card.GUI_SCALE_FACTOR), round(im.size[1]*Card.GUI_SCALE_FACTOR)))
        photo = ImageTk.PhotoImage(image)

        self.front_image = photo
        """

    def __str__(self):
        return f"{self.name:>3}"

    def __eq__(self,other):
        return self.value == other.value

    def __gt__(self,other):
        return self.value > other.value

    def __lt__(self,other):
        return self.value < other.value

    def __ge__(self,other):
        return self.value >= other.value

    def __le__(self,other):
        return self.value <= other.value

    def __repr__(self):
        s = f"Name: {self.name}"
        s += f"\nLong Name: {self.long_name}"
        s += f"\nSuit: {self.suit}"
        s += f"\nSuit Symbol: {self.name[-1]}"
        s += f"\nValue: {self.value}"
        s += f"\nColor: {self.color}"
        # s += f"\nFront Image: {self.front_image}"
        s += f"\nBack Image: {self.back_image}"
        s += f"\nId: {id(self)}"
        return s
'''
class Card:
    # Class variables
    SUITS = ["♤", "♡", "♧", "♢"]
    SUITS2 = ["Spades", "Hearts", "Clubs", "Diamonds"]
    NAMES = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    
    
    # Constructor
    def __init__(self, suit, value):
        # Instance variables
        self.suit = suit     # Ex: "Hearts"
        self.value = int(value)      # Ex: 2...10, 11, 12, 13, 14
        
        if self.suit == "Hearts" or self.suit == "Diamonds":
            self.color = "Red"
        else:
            self.color = "Black"
        
        self.long_name = Card.NAMES[self.value] + " of " + self.suit
        
        if self.value == 10:
            self.name = Card.NAMES[self.value][:2] + Card.SUITS[Card.SUITS2.index[self.suit]]
        else:
            self.name = Card.NAMES[self.value][0] + Card.SUITS[Card.SUITS2.index[self.suit]]
            
        self.back_image = "card_back_red.png"
        self.front_image = self.long_name.replace(" ", "_").lower() + ".png"
    def __str__(self):
        # Output this: 4♡ K♧ 10♢
        s = Card.NAMES[self.value][0]
        
    def set_hidden(self, true_or_false):
        self = true_or_false
        return self
        
    def __eq__(self, other):
        return self.value == other.value
    
    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value
    
    def __ge__(self, other):
        return self.value >= other.value

    def __le__(self, other):
        return self.value <= other.value
    
    def __repr__(self):
        s = f"Name: {self.name}"
        s += f"\nLong Name: {self.long_name}"
        s += f"\nSuit: {self.suit}"
        s += f"\nSuit Symbol: {self.name[-1]}"
        s += f"\nValue: {self.value}"
        s += f"\nFront Image: {self.front_image}"
        s += f"\nBack Image: {self.back_image}"
        s += f"\nId: {id(self)}"
        return s
    
    def build(self):
        for suit in Card.SUITS:
            pass
    
'''