import tkinter as tk
import csv

root = tk.Tk()
root.geometry("500x300")
root.title("My App")

# This is a 2D List
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

# Create and Pack a text widget           
textArea = tk.Text(root, width=32, height=10)
textArea.pack()

# Loop through data and add to text widget
count = 1
for each_student in students:
    textArea.insert(tk.END, f"{count:2}: {each_student[1]}\n")
    count += 1
        
    
def save_data():
    filename = "data.csv"
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(students)
        
def load_data():
    with open('data.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            students2.append(row)
    print(students2)
    
# save_data()
students2 = [ ]
# load_data()

root.mainloop()