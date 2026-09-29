import tkinter as tk
import os
from tkinter import ttk

class UserInputFrame(ttk.Frame):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        userInputButton = ttk.Button(self, text = "Accept Input", command = self.userInputButtonPressed)
        openFileButton = ttk.Button(self, text = "Open File",command = self.openFileButtonPressed)
        self.userInputEntry = ttk.Entry(self)
        runProgramButton = ttk.Button(self, text = "Run Program", command = self.runProgramButtonPressed)
        self.currentFileLabel = ttk.Label(self, text = "No File Selected.")

        self.columnconfigure((0,1,2,3), weight = 1, uniform = 'a')
        self.rowconfigure((0,1), weight = 1, uniform = 'a')
         
        userInputButton.grid(row = 0, column = 3, sticky = 'e')
        openFileButton.grid(row = 0, column = 0, sticky = 'w')
        self.userInputEntry.grid(row = 0, column = 1,columnspan = 2, sticky = 'ns')
        runProgramButton.grid(row = 1, column = 3, sticky = "se")
        self.currentFileLabel.grid(row = 1, column = 0, columnspan = 3,sticky = "sw")
        self.pack(pady = (10,0))
        self.userInputEntry.insert(0, "enter input here...")
        
    def openFileButtonPressed(self):
        labelText = self.parent.controller.handleOpenFile()
        self.currentFileLabel.config(text = f"{labelText}")

    def runProgramButtonPressed(self):
        self.parent.controller.handleRunProgram()

    def userInputButtonPressed(self):
        userInput = self.userInputEntry.get()
        self.parent.controller.handleUserInput(userInput)
