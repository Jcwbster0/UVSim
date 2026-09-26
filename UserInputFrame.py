import tkinter as tk
import os
from tkinter import ttk

class UserInputFrame(ttk.Frame):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        runProgramCommand = parent.controller.runProgramButtonPressed
        userInputCommand = parent.controller.userInputButtonPressed

        userInputButton = ttk.Button(self, text = "Accept Input", command = userInputCommand)
        openFileButton = ttk.Button(self, text = "Open File",command = self.openFileButtonPressed)
        userInputEntry = ttk.Entry(self)
        runProgramButton = ttk.Button(self, text = "Run Program", command = runProgramCommand)
        self.currentFileLabel = ttk.Label(self, text = "No File Selected.")


        self.columnconfigure((0,1,2,3), weight = 1, uniform = 'a')
        self.rowconfigure((0,1), weight = 1, uniform = 'a')
         
        userInputButton.grid(row = 0, column = 3, sticky = 'e')
        openFileButton.grid(row = 0, column = 0, sticky = 'w')
        userInputEntry.grid(row = 0, column = 1,columnspan = 2, sticky = 'ns')
        runProgramButton.grid(row = 1, column = 3, sticky = "se")
        self.currentFileLabel.grid(row = 1, column = 0, columnspan = 3,sticky = "sw")
        self.pack(pady = (10,0))
        userInputEntry.insert(0, "enter input here...")
        
    def openFileButtonPressed(self):
        
        path = self.parent.controller.handleOpenFile()
        filename = os.path.basename(path)
        self.currentFileLabel.config(text = f"{filename}")

