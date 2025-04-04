# HTTP Tutorial 
# https://www.w3schools.com/whatis/whatis_http.asp

# HTTP Methods (We will use GET)
# https://www.w3schools.com/tags/ref_httpmethods.asp

# Tutorial for requests library
# https://realpython.com/python-requests/

# Tutorial for Pillow (PIL)
# https://www.tutorialspoint.com/python_pillow/python_pillow_quick_guide.htm

import tkinter as tk
from PIL import Image, ImageTk
import requests

root = tk.Tk()
root.title("Python Students")
root.geometry("500x500")

# Python Students in each period
students_3F = ["Jaynan Carrasquillo", "Ethan Celano", "Matheus Comandolli",
               "Camilo Contreras", "Nicolas Garcia-Macchiavello", "Amelia Gordon",
               "Hayden Green", "Philip Hanna", "Jace Nguyen", "Thien-Cat Nguyen",
               "Enzo Paparella", "Lars Scholz", "Logan Wagner"]

students_7F = ["Claire Camchong", "Justin Jansen", "Olivia Nguyen", 
               "Parker Rutledge", "Paul Vassiliadis"]

# Get a student from the list
student = students_3F[5]

# Filename in cloud has an underscore in it such as firstname_lastname. Fix the string.
student_fixed = student.replace(" ", "_")

# URL to locate the image in the cloud
image_url = f"https://fullerm-bmchs.github.io/students/2024-2025/{student_fixed}.jpeg"

# Use Pillow (PIL) Library to open the image - Image.open()
# Use requests library to retrieve image from cloud requests.get()
#   Note: Image in the teachers cloud account is stored as a .jpeg file format 
image_jpg = Image.open(requests.get(image_url, stream = True).raw)

# Convert Image to a Tkinter compatible format
image_tkinter = ImageTk.PhotoImage(image_jpg)

# Place the image onto a Tkinter label widget
image_label = tk.Label(root, image = image_tkinter)

# Create a widget for the students name
name = tk.Label(root,text = f"{student}",font=("Arial", 20, "bold"))

# Layout Widgets using Pack
image_label.pack()
name.pack()

# Run the GUI loop - Needs to be last - Infinite Loop
root.mainloop()
