from Card import Card
from Deck import Deck

d = Deck()
d.build()
d.show()
































'''
c1 = Card("Hearts", 12) 
c2 = Card("Spades", 9)

print(c1.name)
print(c1.color)
print("Suit:", c1.suit)
print(c1.long_name)

print(c1.value)

print(c1.front_image)
print(c1.back_image)
print(c1)
print(repr(c1))
'''
'''
d = Deck()
d.build()
player_hand = d.deal()
print("\n")
d.show()
d.return_card(player_hand)
d.show()
'''
'''
print()
d.shuffle().show()

print("\n", d.deal(), d.deal(), d.deal(), d.deal(), "\n")

d.show()


'''