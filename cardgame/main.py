import Deck
import Card

c1 = Card(12, "Hearts") # builds a Queen card
c2 = Deck("Spades", 9)

print(c1.name)
print(c1.long_name)
print(c1.suit)
print(c1.value)
print(c1.color)
#print(c1.front_image)
#print(c1.back_image)
print(c1)
print(repr(c1))