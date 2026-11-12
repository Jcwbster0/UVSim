import tkinter as tk
import os
from tkinter import ttk


class FileEditorFrame(ttk.Frame):
    def __init__(self, parent, colorConfig):
        super().__init__(parent)
        # Create the ttk.Notebook
        self.textWidgets = []
        self.style = ttk.Style()
        self.notebook = ttk.Notebook(parent)
        self.notebook.pack(expand=True, fill="both")
        
        primaryColor = colorConfig.getPrimary()
        secondaryColor = colorConfig.getSecondary()
        textColor = colorConfig.getText()
        # Add a default open tab
        self.newTab()
        self.updateColors(primaryColor, secondaryColor, textColor)

    def updateColors(self, primaryColor, secondaryColor, textColor):
        self.style.configure("TNotebook", background=primaryColor)
        self.style.configure("TNotebook.Tab", background=primaryColor, foreground=textColor)
        self.style.map("TNotebook.Tab", background=[("selected", secondaryColor)])
        # Apply to every open Text widget
        for text in self.textWidgets:
            text.configure(background=secondaryColor, foreground=textColor, insertbackground = textColor)

    def newTab(self, title="Untitled"):
        frame = ttk.Frame(self.notebook) 
        self.notebook.add(frame, text=title)
        textWidget = tk.Text(frame, wrap="word", undo=True)

        textWidget.pack(side="left", expand=True, fill="both")

        # Select the newly created tab
        self.notebook.select(frame)
        self.textWidgets.append(textWidget)
        return textWidget

    def formatMemoryString(self, i):
        if i < 10:
            return f"x0{i}"
        else:
            return f"x{i}"

    def getMemory(self):
        memory = []
        for key in self.entryDict.keys():
            entry = self.entryDict[key]
            string = entry.get()
            memory.append(string)
        return memory

    def updateMemory(self, memory):
        for key in self.entryDict.keys():
            entry = self.entryDict[key]
            entry.delete(0, tk.END)
            entry.insert(0, memory[key])
