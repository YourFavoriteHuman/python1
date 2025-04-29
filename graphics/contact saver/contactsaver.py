import tkinter as tk
import csv

root = tk.Tk()
root.geometry('900x300')
root.title("Contact Saver")
root.attributes('-topmost', True)


valid_users = [ ]
'''

# Create and grid a text widget           
textArea = tk.Text(root, width=32, height=10)
textArea.grid(padx=5)

count = 1
for each_student in students:
    textArea.insert(tk.END, f"{count:2}: {each_student[1]}\n")
    count += 1
'''
    
def save_data():
    filename = "data.csv"
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(username_str.get())        
def load_data():
    with open('data.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            valid_users.append(row)
    print(valid_users)
    
# save_data()
# load_data()

def create_pushed():
    valid_users.append( [username_str.get(), email_str.get(), phone_str.get()] )
    # textArea.insert(tk.END, f"{username_str.get(), email_str.get(), phone_str.get()}\n")
    textArea.insert(tk.END, f"{valid_users}\n")
    valid_users.append( [username_str.get(), email_str.get(), phone_str.get()] )
    print(valid_users)
    username.delete(0, tk.END)
    email.delete(0, tk.END)
    phone.delete(0, tk.END)
    print(textArea.get('1.0', tk.END))

# Create Widgets
username_str = tk.StringVar()
username_label = tk.Label(root, text="Name:")
username = tk.Entry(root, textvariable=username_str, width=40)

email_str = tk.StringVar()
email_label = tk.Label(root, text="Email:")
email = tk.Entry(root, textvariable=email_str, width=40)

phone_str = tk.StringVar()
phone_label = tk.Label(root, text="Phone number:")
phone = tk.Entry(root, textvariable=phone_str, width=40)

login_button = tk.Button(root, text="Add Contact", command=create_pushed)

textArea = tk.Text(root, width=70, height=12)
textArea_label = tk.Label(root, text="All Contacts:")
# textArea.insert(tk.END, f"{username_str.get()}\t{email_str.get()}\t{phone_str.get()}\n")


#textArea.insert(tk.END, "Name\tEmail\tPhone\n")
#textArea.insert(tk.END, "---------------------\n")

#textArea.tag_configure("center", justify='center')
#textArea.tag_add("center", "1.0", "end") # Center the text
textArea.config(state=tk.DISABLED) # Make the text area read-only



# Create a scrollbar

# Layout Widgets

textArea.grid(column=2, row=1, columnspan=2, rowspan=5, padx=5) 
textArea_label.grid(column=2, row=0, columnspan=2)
username_label.grid(pady=5, row=0, column=0, sticky="w")
username.grid(pady=5, row=1, column=0)
email_label.grid(pady=5, row=2, column=0, sticky="w")
email.grid(pady=5, row=3, column=0)
phone_label.grid(pady=5, row=4, column=0, sticky="w")
phone.grid(pady=5, row=5, column=0)
login_button.grid(pady=5, row=6, column=0)

# Run main loop
root.mainloop()

'''
textArea.grid(column=2, row=1, columnspan=2, rowspan=5)
username_label.grid(pady=5, row=0, column=0, sticky="w")
username.grid(pady=5, row=1, column=0)
email_label.grid(pady=5, row=2, column=0, sticky="w")
email.grid(pady=5, row=3, column=0)
phone_label.grid(pady=5, row=4, column=0, sticky="w")
phone.grid(pady=5, row=5, column=0)
login_button.grid(pady=5, row=6, column=0)
'''