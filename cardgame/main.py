from Card import Card
from Deck import Deck
from Pile import Pile
from tkinter import Tk, Label
from PIL import Image, ImageTk
'''
d = Deck()
d.build()
d.shuffle()

player1 = Pile("Player 1 Hand")
player1_balance = 100


stillPlaying = True

while stillPlaying:
    player1_bet = int(input("how much do you want to bet?: "))    
    player1_color = input("Choose red or black: ")
    player1_color = player1_color.title()

    for _ in range(5):
        player1.add_card(d.deal())
     
    print("the following cards were dealt to the player:")   
    player1.show()
    

    count = 0
    
    for each_card in player1.cards:
        print(each_card.color)
    
    exit()        
    if count >= 3:
        print(f"you won since {count} cards were {player1_color}")
        player1_balance += player1_bet
        
    else:
        print(f"you lost since {count} cards were {player1_color}")
        player1_balance -= player1_bet
        
    player1.remove_all()
        
    if player1_balance == 0:
        stillPlaying = False
        
'''

root = Tk()
root.title("Image example")

im = Image.open("7_of_clubs.jpg")
image = im.resize((round(im.size[0]*0.2), round(im.size[1]*0.2)))
photo = ImageTk.PhotoImage(image)

image_label = Label(root, image=photo)
image_label.pack()

root.mainloop()





















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