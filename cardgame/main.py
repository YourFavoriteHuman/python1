from Card import Card
from Deck import Deck
from Pile import Pile

#  make war
d = Deck()
d.build()
d.shuffle()

p1Hand = Pile("Player 1 Hand")
p2Hand = Pile("Player 2 Hand")
p1Table = Pile("Player 1 Table")
p2Table = Pile("Player 2 Table")


d.show()

roundsplayed = 0

gamerunning = True

for i in range(26):
    p1Hand.add_card_to_pile(d.deal())
    p2Hand.add_card_to_pile(d.deal())
print(p1Hand.pile_of_cards)

while gamerunning:
    roundsplayed += 1
    
    #i played, com played, who has higher card?, remove a card and give both to the winner, if they both have to same card, its war. (bothput down 2 cards and compare who has the highest carf)
    
    if not (p1Hand.size() >= 1 and p2Hand.size() >= 1):
        gamerunning = False
        break