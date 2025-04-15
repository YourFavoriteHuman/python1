import tkinter as tk
from tkinter import ttk # TTK adds themes to tk and 6 new widgets

root = tk.Tk()
root.title("Combobox Example")
root.geometry("300x200")


# Define function for combobox before creating widget
def handle_selection(event):
    label1.configure( text = "Selected option: " + selected_option.get() )

label1 = tk.Label(root, text=" ")

# ComboBox Widget
selected_option = tk.StringVar() # Variable mirrors what the combobox is set to
combobox = ttk.Combobox(root, textvariable=selected_option, values=['Album1','Album2'] )
combobox.set('Album1') # Define default value
combobox.bind("<<ComboboxSelected>>", handle_selection) # Ties function to widget

# Layout all widgets
label1.pack(pady=10)
combobox.pack(pady=10)


root.mainloop()