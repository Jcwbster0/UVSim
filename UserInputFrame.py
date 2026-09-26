import tkinter as tk
from tkinter import ttk

class UserInputFrame(ttk.Frame):
    
    def __init__(self, parent):
        super().__init__(parent)

        userInputButton = ttk.Button(self, text = "Accept Input")
        openFileButton = ttk.Button(self, text = "Open File")
        userInputEntry = ttk.Entry(self)
        runProgramButton = ttk.Button(self, text = "Run Program")
        currentFileLabel = ttk.Label(self, text = "No File Selected.")

        self.columnconfigure((0,1,2,3), weight = 1, uniform = 'a')
        self.rowconfigure((0,1), weight = 1, uniform = 'a')
         
        userInputButton.grid(row = 0, column = 3, sticky = 'e')
        openFileButton.grid(row = 0, column = 0, sticky = 'w')
        userInputEntry.grid(row = 0, column = 1,columnspan = 2, sticky = 'ns')
        runProgramButton.grid(row = 1, column = 3, sticky = "se")
        currentFileLabel.grid(row = 1, column = 0, columnspan = 3,sticky = "sw")
        self.pack(pady = (10,0))
        userInputEntry.insert(0, "enter input here...")
        
