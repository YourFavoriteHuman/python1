import tkinter as tk
import csv

root = tk.Tk()
root.geometry('800x500')

root.attributes('-topmost', True)

valid_users = [ ]
'''
students = [["3F","Jaynan Carrasquillo",9],	 		
            ["3F","Ethan Celano",10],	 		
            ["3F","Matheus Comandolli",11],	 		
            ["3F","Camilo Contreras",11],	 		
            ["3F","Nicolas Garcia-Macchiavello",12],	 		
            ["3F","Amelia Gordon",11],	 		
            ["3F","Hayden Green",11],	 		
            ["3F","Philip Hanna",11],	 		
            ["3F","Jace Nguyen",11],	 		
            ["3F","Thien-Cat Nguyen",11],	 		
            ["3F","Enzo Paparella",9],	 		
            ["3F","Lars Scholz",12],	 		
            ["3F","Logan Wagner",11],
            ["7F","Claire Camchong",11],	 		
            ["7F","Justin Jansen",12],	 		
            ["7F","Olivia Nguyen",10],	 		
            ["7F","Parker Rutledge",10],	 		
            ["7F","Paul Vassiliadis",9]]

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
            students2.append(row)
    print(students2)
    
# save_data()
students2 = [ ]
# load_data()

def create_pushed():
    valid_users.append( [username_str.get(), email_str.get() ] )
    print(valid_users)
    username.delete(0, tk.END)
    email.delete(0, tk.END)
    email.delete(0, tk.END)

# Create Widgets
username_str = tk.StringVar()
username_label = tk.Label(root, text="Username:")
username = tk.Entry(root, textvariable=username_str, width=20)
username = tk.Entry(root, textvariable=username_str, width=20)

email_str = tk.StringVar()
email_label = tk.Label(root, text="Email:")
email = tk.Entry(root, textvariable=email_str)

phone_str = tk.StringVar()
phone_label = tk.Label(root, text="Phone number:")
phone = tk.Entry(root, textvariable=phone_str)

login_button = tk.Button(root, text="Add Contact", command=create_pushed)

textArea = tk.Text(root, width=70, height=20)
# Layout Widgets

textArea.grid(column=2, row=1, columnspan=2, rowspan=5)
username_label.grid(pady=5, row=0, column=0)
username.grid(pady=5, row=1, column=0)
email_label.grid(pady=5, row=2, column=0)
email.grid(pady=5, row=3, column=0)
phone_label.grid(pady=5, row=4, column=0)
phone.grid(pady=5, row=5, column=0)
login_button.grid(pady=5, row=6, column=0)

# Run main loop
root.mainloop()