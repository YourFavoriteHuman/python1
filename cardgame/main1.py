from Card import Card
from Deck import Deck
from Pile import Pile
import random
import time


d = Deck()
d.build()
d.shuffle()




p1Hand = Pile("Player 1 Hand")
p2Hand = Pile("Player 2 Hand")
p1Table = Pile("Player 1 Table")
p2Table = Pile("Player 2 Table")

# d.show()

def status():
    print(f"Round: {roundsplayed}  --> Player 1 has {p1Hand.size()} cards. Player 2 has {p2Hand.size()} cards.")


for i in range(26):
    p1Hand.add_card_to_pile(d.deal())
    p2Hand.add_card_to_pile(d.deal())
    
"""
p1Hand.pile_of_cards = [Card(2,"Spades"), 
                        Card(8,"Spades"),
                        Card(13,"Spades")]

p2Hand.pile_of_cards = [Card(2,"Hearts"), 
                        Card(12,"Hearts"),
                        Card(9,"Hearts")]
# print(p1Hand.pile_of_cards)
# print(p1Table.pile_of_cards)
# print([random.choice(p1Hand.pile_of_cards) for i in range(3)])
"""
roundsplayed = 0

gamerunning = True

start_time = time.time()

while gamerunning:
    
    roundsplayed += 1
    
    # if roundsplayed % 100 == 0:
    #    input()
    
    print()
    print()
    
    #i played, com played, who has higher card?, remove a card and give both to the winner, if they both have to same card, its war. (bothput down 2 cards and compare who has the highest carf)
    
    
    if p1Hand.size() >= 1 and p2Hand.size() >= 1:
        p1Table.add_card_to_pile(p1Hand.remove_one_card())
        p2Table.add_card_to_pile(p2Hand.remove_one_card())
        print("Player 1 Dealt: ", end = " ")
        p1Table.show_pile()
        print("Player 2 Dealt: ", end = " ")
        p2Table.show_pile()
        
    else:
        gamerunning = False
        break
    
    # Check for winner
   
    if p1Table.last_played() > p2Table.last_played():
         # Player 1 won
         p1Hand.add_many_to_pile(p2Table.get_all_from_pile())
         p1Hand.add_many_to_pile(p1Table.get_all_from_pile())
         
         # p1Table.show_pile()
         # p2Table.show_pile()
         print("Player 1 Won")
         status()
         
    elif p1Table.last_played() < p2Table.last_played():
         p2Hand.add_many_to_pile(p1Table.get_all_from_pile())
         p2Hand.add_many_to_pile(p2Table.get_all_from_pile())
         # p1Table.show_pile()
         # p2Table.show_pile()
         print("Player 2 Won")
         status()
    else:
        warCount  = 1
        print("\nWAR TIME")
        # War Time
        
        
        while p1Table.last_played() == p2Table.last_played():  
            if p1Hand.size() < 2 or p2Hand.size() < 2:
                print("Cant continue because a player ran out of cards!\n")
                gamerunning = False
                break
                 
            p1Table.add_card_to_pile(p1Hand.remove_one_card())
            p2Table.add_card_to_pile(p2Hand.remove_one_card())
            p1Table.add_card_to_pile(p1Hand.remove_one_card())
            p2Table.add_card_to_pile(p2Hand.remove_one_card())
            print("Player 1 Dealt: ", end = " ")
            p1Table.show_pile()
            print("Player 2 Dealt: ", end = " ")
            p2Table.show_pile()
            warCount += 1
            if warCount == 5:
                input("GAME PAUSED DUE TO AMAZING WAR SEQUENCE. HIT RETURN")
        
            """
            ###################
            print("temp")
            p1Table.show_pile()
            p1Hand.show_pile()
            p2Table.show_pile()
            p2Hand.show_pile()
            print("end of temp")
            ###################
            """
            
            if p1Table.last_played() > p2Table.last_played():
                print("Player 1 won")
                p1Hand.add_many_to_pile(p2Table.get_all_from_pile())
                p1Hand.add_many_to_pile(p1Table.get_all_from_pile())
                status()
                """
                ###################
                print("temp")
                p1Table.show_pile()
                p1Hand.show_pile()
                p2Table.show_pile()
                p2Hand.show_pile()
                print("end of temp")
                ###################
                """
                break
            
            elif p1Table.last_played() < p2Table.last_played():
                print("Player 2 won")
                p2Hand.add_many_to_pile(p1Table.get_all_from_pile())
                p2Hand.add_many_to_pile(p2Table.get_all_from_pile())
                """
                ###################
                print("temp")
                p1Table.show_pile()
                p1Hand.show_pile()
                p2Table.show_pile()
                p2Hand.show_pile()
                print("end of temp")
                """
                status()
                break
        
                
    if gamerunning == False:
        break
        
if p1Hand.size() > p2Hand.size():
    print("Player 1 wins the game!")
elif p1Hand.size() < p2Hand.size():
    print("Player 2 wins the game!")


end_time = time.time()

print(f"The game ran for { (end_time - start_time) * 1000} milliseconds.")
print()