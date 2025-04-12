import tkinter as tk
  
root = tk.Tk()
root.geometry("100x100")
frame = tk.Frame(root, height=100, width=100)
  
  
def change_bg():
    frame.config(background='red')
      
  
button = tk.Button(frame, text="Paint",command=change_bg)
  
  
button.pack()
frame.pack(fill="y", expand=True)
root.mainloop()