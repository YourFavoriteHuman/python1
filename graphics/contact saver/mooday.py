import tkinter as tk

root = tk.Tk()
root.geometry('300x200')

valid_users = [ ]

def create_pushed():
    valid_users.append( [username_str.get(), password_str.get() ] )
    print(valid_users)
    username.delete(0, tk.END)
    password.delete(0, tk.END)
    password.delete(0, tk.END)

# Create Widgets
username_str = tk.StringVar()
username_label = tk.Label(root, text="Username:")
username = tk.Entry(root, textvariable=username_str )

password_str = tk.StringVar()
password_label = tk.Label(root, text="Password:")
password = tk.Entry(root, textvariable=password_str)

login_button = tk.Button(root, text="CREATE ACCOUNT", command=create_pushed)

# Layout Widgets
username_label.pack(pady=5)
username.pack(pady=5)
password_label.pack(pady=5)
password.pack(pady=5)
login_button.pack(pady=5)

# Run main loop
root.mainloop()