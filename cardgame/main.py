from Card import Card
from Deck import Deck
from Pile import Pile
import random

#  make war
d = Deck()
d.build()
d.shuffle()

p1Hand = Pile("Player 1 Hand")
p2Hand = Pile("Player 2 Hand")
p1Table = Pile("Player 1 Table")
p2Table = Pile("Player 2 Table")


# d.show()

roundsplayed = 0

gamerunning = True

for i in range(26):
    p1Hand.add_card_to_pile(d.deal())
    p2Hand.add_card_to_pile(d.deal())
# print(p1Hand.pile_of_cards)
# print(p1Table.pile_of_cards)
# print([random.choice(p1Hand.pile_of_cards) for i in range(3)])
while gamerunning:
    roundsplayed += 1
    
    
    #i played, com played, who has higher card?, remove a card and give both to the winner, if they both have to same card, its war. (bothput down 2 cards and compare who has the highest carf)
    if len(p1Hand.pile_of_cards) > 3:
        p1Table.pile_of_cards = [p1Hand.pile_of_cards.pop(random.randint(0, (len(p1Hand.pile_of_cards) - 1))) for i in range(3)]
    else:
        print("computer wins the game!")
        gamerunning = False
        break
    if len(p2Hand.pile_of_cards) > 3:    
        p2Table.pile_of_cards = [p1Hand.pile_of_cards.pop(random.randint(0, len(p1Hand.pile_of_cards) - 1)) for i in range(3)]
    else:
        print("player wins!")
        gamerunning = False
        break
    print("I played: \n", " ".join(p1Table.pile_of_cards))
    input()
    print("Computer played: \n", " ".join(p2Table.pile_of_cards))
    
    if p1Table.pile_of_cards[-1] > p2Table.pile_of_cards[-1]:
        p1Table.pile_of_cards.extend([p2Table.pile_of_cards.pop(0), p2Table.pile_of_cards.pop(1), p2Table.pile_of_cards.pop(-1)])
        print("\n", p1Table.pile_of_cards, "\n", p1Hand.pile_of_cards)
        print("Player win")
        
    elif p2Table.pile_of_cards[-1] > p1Table.pile_of_cards[-1]:
        p2Table.pile_of_cards.extend([p1Table.pile_of_cards.pop(0), p1Table.pile_of_cards.pop(1), p1Table.pile_of_cards.pop(-1)])
        print("\n",p2Table.pile_of_cards, "\n", p1Hand.pile_of_cards)
        print("computer win")
        
    elif p1Table.pile_of_cards[-1] == p2Table.pile_of_cards[-1]:
        print("war time!")
        p1Table.pile_of_cards = [random.choice(p1Hand.pile_of_cards) for i in range(2)]
        p2Table.pile_of_cards = [random.choice(p2Hand.pile_of_cards) for i in range(2)]
        
        if p1Table.pile_of_cards[-1] > p2Table.pile_of_cards[-1]:
            p1Table.pile_of_cards.extend([p2Table.pile_of_cards.pop(0), p2Table.pile_of_cards.pop(1), p2Table.pile_of_cards.pop(-1)])
            print(p1Table.pile_of_cards)
            print("Player win")
            
        elif p2Table.pile_of_cards[-1] > p1Table.pile_of_cards[-1]:
            p2Table.pile_of_cards.extend([p1Table.pile_of_cards.pop(0), p1Table.pile_of_cards.pop(1), p1Table.pile_of_cards.pop(-1)])
            print(p2Table.pile_of_cards)
            print("computer win")
            
    elif p1Table.pile_of_cards[1] == p2Table.pile_of_cards[1]:
        print("war time!")
        p1Table.pile_of_cards = [random.choice(p1Hand.pile_of_cards) for i in range(2)]
        p2Table.pile_of_cards = [random.choice(p2Hand.pile_of_cards) for i in range(2)]
        
        if p1Table.pile_of_cards[-1] > p2Table.pile_of_cards[-1]:
            p1Table.pile_of_cards.extend([p2Table.pile_of_cards.pop(0), p2Table.pile_of_cards.pop(1), p2Table.pile_of_cards.pop(-1)])
            print(p1Table.pile_of_cards)
            print("Player win")
            
        elif p2Table.pile_of_cards[-1] > p1Table.pile_of_cards[-1]:
            p2Table.pile_of_cards.extend([p1Table.pile_of_cards.pop(0), p1Table.pile_of_cards.pop(1), p1Table.pile_of_cards.pop(-1)])
            print(p2Table.pile_of_cards)
            print("computer win")
            
    elif p1Table.pile_of_cards[0] == p2Table.pile_of_cards[0]:
        print("war time!")
        p1Table.pile_of_cards = [random.choice(p1Hand.pile_of_cards) for i in range(2)]
        p2Table.pile_of_cards = [random.choice(p2Hand.pile_of_cards) for i in range(2)]
        
        if p1Table.pile_of_cards[-1] > p2Table.pile_of_cards[-1]:
            p1Table.pile_of_cards.extend([p2Table.pile_of_cards.pop(0), p2Table.pile_of_cards.pop(1), p2Table.pile_of_cards.pop(-1)])
            print(p1Table.pile_of_cards)
            print("Player win")
            
        elif p2Table.pile_of_cards[-1] > p1Table.pile_of_cards[-1]:
            p2Table.pile_of_cards.extend([p1Table.pile_of_cards.pop(0), p1Table.pile_of_cards.pop(1), p1Table.pile_of_cards.pop(-1)])
            print(p2Table.pile_of_cards)
            print("computer win")
        
    
    if not (p1Hand.size() >= 1 and p2Hand.size() >= 1):
        gamerunning = False
        break