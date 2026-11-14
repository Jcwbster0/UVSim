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
        style.configure("Custom.TEntry", fieldbackground=self.colorConfig.getSecondary(), foreground=self.colorConfig.getText())
        style.configure("Placeholder.TEntry", fieldbackground=self.colorConfig.getSecondary(), foreground="grey")

        super().__init__(parent, style = "Custom.TFrame")

        self.placeholder = "enter input here..."

        # All the buttons
        userInputButton = ttk.Button(
            self, 
            text = "Accept Input", 
            command = self.userInputButtonPressed, 
            style = "Custom.TButton"
        )
        openFileButton = ttk.Button(
            self, 
            text = "Open File",
            command = self.openFileButtonPressed, 
            style = "Custom.TButton"
        )
        runProgramButton = ttk.Button(
            self, 
            text = "Run Program", 
            command = self.runProgramButtonPressed, 
            style = "Custom.TButton"
        )
        colorSettingsButton = ttk.Button(
            self, 
            text = "Color Settings", 
            command = self.openColorSettings, 
            style = "Custom.TButton"
        )
        saveFileButton = ttk.Button(
            self,
            text = "Save File",
            command = self.saveFileButtonPressed,
            style = "Custom.TButton"
                )

        newFileTabButton = ttk.Button(
            self,
            text = "Open New Tab",
            command = self.newFileTabButtonPressed,
            style = "Custom.TButton"
        )

        deleteFileTabButton = ttk.Button(
            self,
            text = "Delete Tab",
            command = self.deleteFileTabButtonPressed,
            style = "Custom.TButton"
        )

        # User input field
        self.userInputEntry = ttk.Entry(
            self, 
            style = "Custom.TEntry"
        )


        self.columnconfigure((0,1,2,3,4), weight = 1, uniform = 'a')
        self.rowconfigure((0,1), weight = 1, uniform = 'a')

        # File Management
        pad = 5
        openFileButton.grid(row = 0, column = 0, sticky = "ew", padx = pad, pady = pad)
        saveFileButton.grid(row = 0, column = 3, sticky = "ew", padx = pad, pady = pad)
        runProgramButton.grid(row = 0, column = 1, sticky = "ew", padx = pad, pady = pad)
        newFileTabButton.grid(row = 1, column = 3, sticky = "ew", padx = pad, pady = pad)
        deleteFileTabButton.grid(row = 1, column = 4, sticky = "ew", padx = pad, pady = pad)

        # Input Management
        self.userInputEntry.grid(row = 1, column = 0, padx = pad, pady = pad)
        userInputButton.grid(row = 1, column = 1, sticky = "ew", padx = pad, pady = pad)

        # Color Chooser Button
        colorSettingsButton.grid(row = 0, column = 4, sticky = "ew", padx = pad, pady = pad)

        
        self.pack(pady = (10,0))
        self.userInputEntry.insert(0, self.placeholder)

        self.userInputEntry.bind("<FocusIn>", self.clearPlaceholder)
        self.userInputEntry.bind("<FocusOut>", self.restorePlaceholder)

    def clearPlaceholder(self, event):
        if self.userInputEntry.get() == self.placeholder:
            self.userInputEntry.delete(0, tk.END)
            self.userInputEntry.config(style="Custom.TEntry")

    def restorePlaceholder(self, event):
        if self.userInputEntry.get() == "":
            self.userInputEntry.insert(0, self.placeholder)
            self.userInputEntry.config(style="Placeholder.TEntry")

    def newFileTabButtonPressed(self):
        self.parent.controller.handleNewTab()
        return

    def deleteFileTabButtonPressed(self):
        self.parent.controller.handleDeleteTab()
    
    def openFileButtonPressed(self):
        labelText = self.parent.controller.handleOpenFile()
    #    self.currentFileLabel.config(text = f"{labelText}")

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

    def saveFileButtonPressed(self):
        self.parent.controller.handleSaveFile()
