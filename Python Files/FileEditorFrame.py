import tkinter as tk
import os
from tkinter import ttk


class FileEditorFrame(ttk.Frame):
    def __init__(self, parent, colorConfig):
        super().__init__(parent)
        # Create the ttk.Notebook
        self.frameDict = {}
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
        for text in self.frameDict.values():
            text.configure(background=secondaryColor, foreground=textColor, insertbackground = textColor)

    def newTab(self, title="Untitled"):
        frame = ttk.Frame(self.notebook) 
        self.notebook.add(frame, text=title)
        textWidget = tk.Text(frame, wrap="word", undo=True, font=("Courier", 14))

        textWidget.pack(side="left", expand=True, fill="both")

        # Select the newly created tab
        self.notebook.select(frame)
        self.frameDict[str(frame)] = textWidget
        return textWidget

    def parseFile(self,fileString):
        return [line.strip() for line in fileString.splitlines()]

    def getMemory(self):
        frameId = self.notebook.select()
        selectedFrame = self.frameDict.get(frameId)
        if selectedFrame:
            fileString = selectedFrame.get("1.0", "end-1c")
            memory = self.parseFile(fileString)
            return memory

    def updateMemory(self, memory):
        frame = self.frameDict[self.notebook.select()]
        frame.delete("1.0", "end")
        frame.insert("end", "\n".join(memory))
        
