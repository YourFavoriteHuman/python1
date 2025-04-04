import tkinter as tk

root = tk.Tk()

# Setting some window properties
root.title('Card Table')
root.configure(bg = "green")
root.geometry("800x800")

# Display Widgets is a 2-step process

# 1) Define the widget(s)

images = []
images.append(tk.PhotoImage(file="ace_of_clubs.png"))
images.append(tk.PhotoImage(file="10_of_hearts.png"))

label0 = tk.Label(root, text="Player 1", font=("Arial", 24, "bold"), anchor="sw")
label1 = tk.Label(root, image=images[0], borderwidth=5, relief="solid")
label2 = tk.Label(root, image=images[1], borderwidth=5, relief="solid")

# 2) Layout the widget(s) on the window

label0.pack()
label1.pack(side=tk.LEFT, padx=5)
label2.pack(side=tk.LEFT, padx=5)


root.mainloop()




