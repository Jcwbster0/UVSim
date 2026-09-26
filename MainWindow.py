import tkinter as tk
from tkinter import ttk
import UserInputFrame
import FileOutputFrame

class MainWindow(tk.Tk):
    
    def __init__(self, title, size, controller): 
       super().__init__() 
       self.title(title)
       self.geometry(f"{size[0]}x{size[1]}")
       self.minsize(size[0], size[1])
       self.title = title
       self.controller = controller

       #Disable resizing
       self.resizable(False, False)
       #initialize ui widgets here
        
       self.userInputFrame = UserInputFrame.UserInputFrame(self) 
       self.FileOutputFrame = FileOutputFrame.FileOutputFrame(self)
       

       
       
       self.mainloop()
        
