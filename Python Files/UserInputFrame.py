import tkinter as tk
import os
from tkinter import ttk
import ColorSettingsWindow

class UserInputFrame(ttk.Frame):
    
    def __init__(self, parent, colorConfig):
        self.parent = parent
        self.colorConfig = colorConfig

        # Color Configuration
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Custom.TFrame", background=self.colorConfig.getPrimary())
        style.configure("Custom.TButton", background=self.colorConfig.getSecondary(), foreground=self.colorConfig.getText())
        style.configure("Custom.TLabel", background=self.colorConfig.getPrimary(), foreground=self.colorConfig.getText())


        super().__init__(parent, style = "Custom.TFrame")

        self.placeholder = "enter input here..."

        userInputButton = ttk.Button(self, text = "Accept Input", command = self.userInputButtonPressed, style = "Custom.TButton")
        openFileButton = ttk.Button(self, text = "Open File",command = self.openFileButtonPressed, style = "Custom.TButton")
        self.userInputEntry = ttk.Entry(self, foreground="grey")
        runProgramButton = ttk.Button(self, text = "Run Program", command = self.runProgramButtonPressed, style = "Custom.TButton")
        self.currentFileLabel = ttk.Label(self, text = "No File Selected.", style = "Custom.TLabel")
        colorSettingsButton = ttk.Button(self, text = "Color Settings", command = self.openColorSettings, style = "Custom.TButton")

        self.columnconfigure((0,1,2,3), weight = 1, uniform = 'a')
        self.rowconfigure((0,1,2), weight = 1, uniform = 'a')

        # File Management
        openFileButton.grid(row = 0, column = 0, sticky = "e")
        self.currentFileLabel.grid(row = 0, column = 1)
        runProgramButton.grid(row = 2, column = 0, sticky = "e")

        # Input Management
        self.userInputEntry.grid(row = 2, column = 2)
        userInputButton.grid(row = 2, column = 3, sticky = "w")

        # Color Chooser Button
        colorSettingsButton.grid(row = 0, column = 3, sticky = "w")

        
        self.pack(pady = (10,0))
        self.userInputEntry.insert(0, self.placeholder)

        self.userInputEntry.bind("<FocusIn>", self.clearPlaceholder)
        self.userInputEntry.bind("<FocusOut>", self.restorePlaceholder)

    def clearPlaceholder(self, event):
        if self.userInputEntry.get() == self.placeholder:
            self.userInputEntry.delete(0, tk.END)
            self.userInputEntry.config(foreground="black")

    def restorePlaceholder(self, event):
        if self.userInputEntry.get() == "":
            self.userInputEntry.insert(0, self.placeholder)
            self.userInputEntry.config(foreground="grey")
    
    def openFileButtonPressed(self):
        labelText = self.parent.controller.handleOpenFile()
        self.currentFileLabel.config(text = f"{labelText}")

    def runProgramButtonPressed(self):
        self.parent.controller.handleRunProgram()

    def userInputButtonPressed(self):
        userInput = self.userInputEntry.get()
        if userInput == self.placeholder:
            userInput = ""
        self.parent.controller.handleUserInput(userInput)
        
    def openColorSettings(self):
        ColorSettingsWindow.ColorSettingsWindow(
            self.parent,
            self.colorConfig
        )