#############################################################
# This program will not run on CodeHS.com
# CodeHS.com does not support the requests library
#############################################################



import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests

root = tk.Tk()
root.title("Face Flashcards")
root.geometry("325x540+50+0")
root.resizable(False, False)

currentIndex = 0



students = ["Jaynan Carrasquillo", "Ethan Celano", "Matheus Comandolli",
               "Camilo Contreras", "Nicolas Garcia-Macchiavello", "Amelia Gordon",
               "Hayden Green", "Philip Hanna", "Jace Nguyen", "Thien-Cat Nguyen",
               "Enzo Paparella", "Lars Scholz", "Logan Wagner", "Claire Camchong", 
               "Justin Jansen", "Olivia Nguyen", "Parker Rutledge", 
               "Paul Vassiliadis"]

faculty = ["Thomas Doyle","Nick Pavgouzas","Vincent Bello",
	"Mark Cammack","Debra Cooper","Marvin Snyder",
	"Astrid Aaron","Madeleine Aiello","Felix Alvarez",
	"Amphoe Arriola","Robyn Baltar","Claudette Banciella",
	"James Barker","Kristy Belden","Ashley Belle",
	"Kay Bencen","Kristi Bergman","Neil Bittong",
	"Joan Bombich","Ana Borges","Gina Bresnahan",
	"Lisa Brogan","Peter Brown","Luisa Buck",
	"Megan Cantor","Kelly Carbone","Taylor Cascio",
	"Matthew Casey","Chase Cassady","Dayra Castro",
	"Sarah Chambers","Sasha Chavez","Cherry Mackenzie",
	"Helen Chwalisz","Brooke Cimmino","Rickey Claitt",
	"Jennifer Connell","Stephen Corrie","Mimi Costa",
	"Eric Cote","Lisa Crespo","Christopher Cruz",
	"Olivia Currea","Colin Cyrus","Krista Davila",
	"Micah Davis","Lizbeth Del-Giudice","Lucie Dempsey",
	"Theresa DePrinzio","Claudy Devilien","Jennifer Doig",
	"Deirdre Drinkall","Kimberly Driver","Isabel DuQue",
	"Lynn Eberly","Christopher Emig","Jennifer Etscorn",
	"Genevieve Fable","Ryan Fleming","James Foltz",
	"Jean Ford","Joe Forney","Mark Fortier",
	"Mark Fuller","Armani Garrick","Alex Garver",
	"Annelise Gavillan-Rivera","Michael Geelan","Amy Geltz",
	"AnaMaria Gonzalez","Janet Gose","Mary Grady",
	"Chris Grant","Anita Gros","Ines Gurley",
	"Jorge Haddock-Morales","Tom Hage","Cathy Harper-Drake",
	"Mary Hart","Heidi Hattabaugh","Matt Hedrick",
	"Tammy Helenthal","Gina Helms","Siobhan Henderson",
	"Eric Hennes","Michael Hennessy","Eli Hernandez",
	"Joshua Hobart","Julia Ingler","Julio Irizarry",
	"Ruthven Jackie","Sue Jackson","Miko Jimenez",
	"Haylie Jones","Larissa Jour-Amadea","Cynthia Kearney",
	"JP Kuhlman","Jeff LaBelle","Tom Laegeler",
	"Mike Laguardia","Ben Leer","Allison Lehnen",
	"Nicole Leonhardt","Rachel Luckenbill","Rosaly Lugaro-Vega",
	"Rosaly Lugaro","Sarah Luter","Eric Madigan",
	"Susan Madigan","Mike Malatesta","Adam Mantovani",
	"Jerry Mathis","Adrian Mayer","Gorden Mayes",
	"Gracie Mazanec","Jonathan McClintock","Nichole Mehlich",
	"Tony Mehlich","Rachel Meyers","Daniel Minnich",
	"Eric Moskowitz","Esther Moss","Kristin Mudd-Lounder",
	"Bruce Mulford","Tracey Murray","Anhvu Nguyen",
	"Lane Nicolay","Kyle Nunez","Paul O'Grady",
	"Kate O'Reilly","Angela Olesen","Jimmy Ortiz",
	"Michael Panico","Christopher Pass","Patrick Philbin",
	"Kate Piscopo","Kelly-Ann Pounds","Andrew Prince",
	"Betty Protz","Mary Pryor","Jack Ramsey",
	"Brian Reim","Zachary Rimmele","Romy Rivera",
	"Ainsley Robertson","Paola Rodriguez","Clifford Roer",
	"Lynette Sarofim","Maria Scarabino","Michael Sciotto",
	"Alexandra-Padula Senior","William Shade","Erin Shank",
	"Carlin Shaw","Barbara Sickler","Kathryn Smith",
	"Stacy Snelling","Robbie Snyder","Victor Sorondo",
	"Patrick Stallings","Tanya Starrett","Paula Steadman",
	"Kimberly Story","Kimberly Straw","Joanne Strickler",
	"Joseph Stuart","Jared Tatum","Linda Tatum",
	"Alison Tett","Amanda Thomas","John Timmes",
	"Diana Tompkins","Andy Urban","Stefanie Valdes",
	"Michelle Vazquez-Langan","Carolista Ware","John Wasman-",
	"John Wasman","Lisa Weger","Tyler Wellington",
	"Kristi Wells","Joan Wheeler","Mark White",
	"Bryan Wilk","Doug Willett","Shawn Willox",
	"Troy Wilson","Susan Wofford","Andre Wright",
	"Raymond Wynne","Dee Zoellick"]

student = students[currentIndex]
faculty1 = faculty[currentIndex]
student_fixed = student.replace(" ", "_")
faculty_fixed = faculty1.replace(" ", "_")
person = student
image_url = f"https://fullerm-bmchs.github.io/students/2024-2025/{student_fixed}.jpeg"
image_jpg = Image.open(requests.get(image_url, stream = True).raw)    
image_tkinter = ImageTk.PhotoImage(image_jpg)


def prev():
    # You can change the names of the variables
    # Any variables outside a function that need to be changed inside a function
    # will require the GLOBAL keyword as below
    global currentIndex
    currentIndex -= 1
    if combobox.get() == "Students":
        if currentIndex == -len(students):
            currentIndex = 0
    elif combobox.get() == "Faculty":
        if currentIndex == -len(faculty):
            currentIndex = 0 
    print(currentIndex)
    change_pic()

    
def next():
    # You can change the names of the variables
    global currentIndex
    currentIndex += 1
    if combobox.get() == "Students":
        if currentIndex == len(students):
            currentIndex = 0
    elif combobox.get() == "Faculty":
        if currentIndex == len(faculty):
            currentIndex = 0
    print(currentIndex)
    change_pic()
    
def first():
    global currentIndex
    currentIndex = 0
    change_pic()
    
def last():
    global currentIndex
    currentIndex = -1    
    change_pic()
    
def change_pic():
    global currentIndex, image_tkinter
    person_fixed = person[currentIndex].replace(" ", "_")
    person1 = person[currentIndex]
    # You can change the names of the variables
    if combobox.get() == "Faculty":
        image_url = f"https://fullerm-bmchs.github.io/students/2024-2025/faculty/{person_fixed}.jpeg"
        print("chamged ")
    elif combobox.get() == "Students":
        image_url = f"https://fullerm-bmchs.github.io/students/2024-2025/{person_fixed}.jpeg"
    
    # student = students[currentIndex]
    
    print(f"{person_fixed=}")
    image_jpg = Image.open(requests.get(image_url, stream = True).raw)    
    image_resized = image_jpg.resize((320, 400))
    image_tkinter = ImageTk.PhotoImage(image_resized)
    #image_label = tk.Label(root, image = image_tkinter)
    image_label.grid(row=0, column=2)
    #name = tk.Label(root,text = f"{person1}",font=("Arial", 20, "bold"))
    print(person[currentIndex])
    image_label.configure(image = image_tkinter)
    name.configure(text = f"{person[currentIndex]}",font=("Arial", 20, "bold"))
    name.update()
    # name.grid_forget()
    name.grid(row=1, column=2, columnspan=2, padx=5, pady=10)

    
    

def combo_changed(event):
    global person, currentIndex
    if combobox.get() == "Faculty":
        currentIndex = 0
        person = faculty
        print("CHANGED")

    elif combobox.get() == "Students":
        currentIndex = 0
        person = student
        change_pic()
    change_pic()
    
    
'''
def handle_selection(event):
    name.configure( text = "Selected option: " + selected_option.get() )
''' 
# Python Students in each periodvvv

root.attributes('-topmost', True)


# This variable will change to point to a different set of pictures (Album)
# As needed by the code.
person = students

# frame = tk.Frame(root, height=100, width=100)
# def change_bg():
    # frame.config(background='red')
    # pass
'''
student = students[currentIndex]
student_fixed = student.replace(" ", "_")
image_url = f"https://fullerm-bmchs.github.io/students/2024-2025/{student_fixed}.jpeg"
image_jpg = Image.open(requests.get(image_url, stream = True).raw)    
image_tkinter = ImageTk.PhotoImage(image_jpg)
'''
# button = tk.Checkbutton(frame, text="Paint",command=change_bg)
# Create widgets

image_label = tk.Label(root, image = image_tkinter)
name = tk.Label(root,text = f"{person[currentIndex]}",font=("Arial", 20, "bold"))
button1 = tk.Button(text="Prev", command=prev)
button2next = tk.Button(text="Next", command=next)
button3end = tk.Button(text="Last", command=last)
button4beginning = tk.Button(text="First", command=first)
button5quit = tk.Button(text="Quit", command=quit)
selected_option = tk.StringVar() # Variable mirrors what the combobox is set to
combobox = ttk.Combobox(root, values=['Students','Faculty'], state="readonly")
combobox.set('Students') # Define default value
combobox.bind("<<ComboboxSelected>>", combo_changed) # Ties function to widget
# albumlist = tk.Listbox(selectmode="single")
# albumlist.insert(1, "Students")
# albumlist.insert(2, "Faculty")
# Layout Widgets using grid

# button.grid(row=0, column=0)
# frame.grid(row=0, column=0,)
image_label.grid(row=0, column=2)
name.grid(row=1, column=2, columnspan=2, padx=5, pady=10)
button1.grid(row=3, column=2, padx=0, pady=10, sticky="w")
button2next.grid(row=3, column=2,padx =5, pady=10, sticky="e")
button3end.grid(row=2, column=2,padx =5, pady=10, sticky="e")
button4beginning.grid(row=2, column=2, padx=0, pady=10, sticky="w")
button5quit.grid(row=3, column=2, padx=0, pady=10, sticky="s")
combobox.grid(row=2, column=2, columnspan=2,padx=5, pady=10)
# albumlist.grid(row=1, column=3)
# Run the GUI loop - Needs to be last - Infinite Loop


root.mainloop()

# Grading will focus on the following goals
# 1) The program uses 2 buttons
# 2) The program uses 1 combobox
# 3) The program allows the picture gallery to be viewed forwards and backwards
# 4) The program allows the selection of an album (students or faculty)
# 5) The code runs without errors