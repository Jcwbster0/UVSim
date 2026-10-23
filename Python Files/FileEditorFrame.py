import tkinter as tk
import os
from tkinter import ttk


class FileEditorFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0)
        scrollBar = ttk.Scrollbar(self, command=canvas.yview)
        canvas.configure(yscrollcomman=scrollBar.set)
        scrollable_frame = ttk.Frame(canvas)
        frame_window = canvas.create_window(
            (0, 0), window=scrollable_frame, anchor="nw"
        )
        scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.bind(
            "<Configure>", lambda e: canvas.itemconfig(frame_window, width=e.width)
        )

        self.placeholder = "+0000"
        self.entryDict = {}
        self.labelDict = {}
        self.addressFrameDict = {}
        for i in range(100):
            entryNum = i
            labelText = self.formatMemoryString(i)
            addressFrame = ttk.Frame(scrollable_frame)
            entry = ttk.Entry(addressFrame, foreground="grey")
            entry.insert(0, self.placeholder)
            label = ttk.Label(addressFrame, text=labelText)

            self.addressFrameDict[entryNum] = addressFrame
            self.entryDict[entryNum] = entry
            self.labelDict[entryNum] = label

            for key in self.entryDict.keys():
                entry = self.entryDict[key]
                label = self.labelDict[key]
                addressFrame = self.addressFrameDict[key]
                label.pack(side="left", expand=True)
                entry.pack(side="left", expand=True)
                addressFrame.pack(anchor="center", expand=True)
        scrollBar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        self.pack(side="left", fill="both", expand=False)

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
