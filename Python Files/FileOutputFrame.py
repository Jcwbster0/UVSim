import tkinter as tk
from tkinter import ttk

# Frame where all the text outputs go
class FileOutputFrame(ttk.Frame):
    def __init__(self, parent, colorConfig):
        super().__init__(parent)

        self.colorConfig = colorConfig
        self.outputFrame = tk.Text(
            self, 
            bg= self.colorConfig.getSecondary(),    # Background Color
            fg= self.colorConfig.getText(),         # Text Color
            font=("Courier", 14),                   # Monospace font for aligned spacing
            wrap="word",                            # Don't split words mid-line
            state="disabled",                       # Start disabled so user can't manually type over logs
            width = 30,
            height = 10
        )

        self.outputFrame.tag_config(
            "write",
            foreground = self.colorConfig.getText(),
            font = ("Courier", 14)
        )
        self.outputFrame.tag_config(
            "system",
            foreground = self.colorConfig.getPrimary(),
            font = ("Courier", 8, "italic")
        )
        self.outputFrame.tag_config(
            "error",
            foreground = "red",
            font = ("Courier", 14)
        )
        
        scrollBar = ttk.Scrollbar(self, command = self.outputFrame.yview)
        self.outputFrame.pack(side = "left", fill = "both", expand = True)
        scrollBar.pack(side = "right", fill = "y")
        self.pack(side = "left", fill = "both", expand = True)
        
    def pushToOutput(self, msg, msgType = "system"):
        if msgType == "system":
            msg = "\n [CPU] " + msg
        elif msgType == "error":
            msg = "\n ERROR: " + msg
        else:
            msg = "\n" + msg

        self.normalState()
        self.outputFrame.insert(tk.END, msg, msgType)
        self.outputFrame.see(tk.END)
        self.disabledState()
        
    def normalState(self):
        self.outputFrame.config(state="normal")

    def disabledState(self):
        self.outputFrame.config(state="disabled")
