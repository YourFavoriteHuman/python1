from tkinter import Tk, Label
from PIL import Image, ImageTk
from Card import Card
from Deck import Deck
from Pile import Pile

# Define the root Playing Window
root = Tk()
root.title("Card Game Example")
root.geometry('600x400')
root.configure(background='green')

# Define decks and players
d = Deck()
d.build()
d.shuffle()
player1 = Pile("Player 1 Hand")
player2 = Pile("Player 2 Hand")

# Deal 5 cards to a player
for _ in range(5):
    player1.add_card_to_pile( d.deal() )
    player2.add_card_to_pile( d.deal() )

# Display player1 pile name on game board in row 0
player1_label = Label(root, text=player1.name )
player1_label.grid(row=0,column=0,padx=10,pady=10)

# Display player1 pile_of_Cards on game board in row 1
for col,each_card in enumerate(player1.pile_of_cards):
    print(each_card)
    image_label = Label(root, image=each_card.front_image)
    image_label.grid(row=1,column=col,padx=10,pady=10)

# Display player2 pile name on game board in row 2
player2_label = Label(root, text=player2.name )
player2_label.grid(row=2,column=0,padx=10,pady=10)

# Display player2 pile_of_Cards on game board in row 3
for col,each_card in enumerate(player2.pile_of_cards):
    image_label = Label(root, image=each_card.front_image)
    image_label.grid(row=3,column=col,padx=10,pady=10)

root.mainloop()