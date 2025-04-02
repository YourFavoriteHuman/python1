# https://www.pythonguis.com/tkinter-tutorial/

import tkinter as tk
from PIL import Image, ImageTk
# import PIL as p

root = tk.Tk()

scr_width = int(root.winfo_screenwidth() * 0.40)
scr_height = int(root.winfo_screenheight() * 0.40)


# Setting some window properties
root.title("Ocean")
root.configure(background="royalblue",)# activebackground="green"
#root.minsize(200, 200)
#root.maxsize(500, 500)
root.geometry(f"{scr_width}x{scr_height}+700+400")
#root.geometry("4000x3000")
#root.resizable(False, False)
root.attributes('-topmost', True)
#oot.update()

quote = tk.Label(root, text="Nothing will work unless you do.", bg="royal blue", fg="red")
author = tk.Label(root, text="- Maya Angelo", bg="royal blue")


button = tk.Button(command=quit, bg="royal blue", text="yarrrrrrr", cursor="hand1", )
textfield = tk.Text(cursor="xterm", )

'''
for i in range(1,4):
    root.geometry(f"{int(scr_width/i)}x{int(scr_height/i)}")
'''

# image = tk.PhotoImage(file="pokemont.png")
image = Image.open("pokemont.png")
resized_image = image.resize((400, 300))
photo = ImageTk.PhotoImage(resized_image)
picture = tk.Label(root, image=photo, bg="royal blue")

textfield.pack()
button.pack()
picture.pack()
quote.pack()
author.pack()

root.mainloop()