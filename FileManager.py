import os
from tkinter import filedialog, messagebox

class FileManager:
    
    def __init__(self):
        return

    def openFile(self):
        filePath = self.promptForFile()
        defaultLines = []
        if not filePath:
            return (defaultLines,  "Unable to Read File")

        with open(filePath, "r") as file:
            lines = file.readlines()
            lines, errCode = validateFile(lines)
            switch errCode:
                case 0: return (lines,filePath)
                case 1: return (defaultLines,"Error: .txt file expected")
                case 2: return (defaultLines, "Error: invalid opcode")
                case 3: return (defaultLines, "Error: memory exceeded 100 words.")
                case 4: return ()

    def promptForFile(self):
       filePath = filedialog.askopenfilename(title="Choose a File", filetypes = [("Text Files", "*.txt")])
       return filePath
    
    def validate_file(filePath):
        if not filePath.endswith(".txt"): return (False, 1)
            #needs to check for 
            #no halt code, incorrect length, incorrect input/opcodes

    #validate file
        return True
