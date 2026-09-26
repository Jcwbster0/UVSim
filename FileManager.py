import os
from tkinter import filedialog, messagebox

class FileManager:
    
    def __init__(self):
        return
    def promptForFile(self):
       filePath = filedialog.askopenfilename(title="Choose a File", filetypes = [("Text Files", "*.txt")])
       return filePath

