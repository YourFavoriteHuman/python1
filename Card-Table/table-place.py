import tkinter as tk

root = tk.Tk()

# Setting some window properties
root.title('Card Table')
root.configure(bg = "green")
root.geometry("800x800")

# Display Widgets is a 2-step process

# 1) Define the widget(s)

root.attributes('-topmost', True)

images = []
images.append(tk.PhotoImage(file="ace_of_clubs.png"))
images.append(tk.PhotoImage(file="10_of_hearts.png"))
images.append(tk.PhotoImage(file="Jaynan_Carrasquillo.png"))
print(tk.PhotoImage(file="Jaynan_Carrasquillo.png").width())
print(tk.PhotoImage(file="Jaynan_Carrasquillo.png").height())

label0 = tk.Label(root, text="Player 1", font=("Arial", 24, "bold"))
label1 = tk.Label(root, image=images[0], borderwidth=5, relief="solid")
label2 = tk.Label(root, image=images[1], borderwidth=5, relief="solid")
label3 = tk.Label(root, image=images[2], relief="solid")

# 2) Layout the widget(s) on the window

label0.place(x=10, y=10)
label1.place(x=10, y=50)
label2.place(x=80, y=50)
label3.place(x=10, y=390)

root.mainloop()





