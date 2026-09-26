import tkinter as tk
from tkinter import ttk

class FileOutputFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        outputFrame = tk.Text(
                self, 
                bg="#1e1e1e",      # Dark background
                fg="#d4d4d4",      # Default light text
#insertbackground="white", # Cursor color
                font=("Courier", 14),      # Monospace font for aligned spacing
                wrap="word",       # Don't split words mid-line
                state="disabled"   # Start disabled so user can't manually type over logs
                )
        scrollBar = ttk.Scrollbar(self, command = outputFrame.yview)

        outputFrame.pack(side = "left", fill = "both", expand = True)
        scrollBar.pack(side = "right", fill = "y", expand = True)
        self.pack(fill = "both", expand = True)
        


