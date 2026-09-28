import os
from tkinter import filedialog, messagebox

class FileManager:
    
    def __init__(self):
        return

    def openFile(self):
        filePath = self.promptForFile()
        defaultLines = []
        if not filePath or filePath[-4:] != ".txt":
            return (defaultLines,  "Error: .txt file expected")

        with open(filePath, "r") as file:
            lines = [line.rstrip("\n")for line in file.readlines()]
            errCode = self.validateFile(lines)
            match errCode:
                case 0: return (lines,os.path.basename(filePath))
                case 1: return (defaultLines,"Error: no HALT(43) code")
                case 2: return (defaultLines, "Error: invalid opcode")
                case 3: return (defaultLines, "Error: memory exceeded 100 words.")

    def promptForFile(self):
       filePath = filedialog.askopenfilename(title="Choose a File", filetypes = [("Text Files", "*.txt")])
       return filePath
    
    def validateFile(self, lines):
        includes_halt = False
        if len(lines) > 100:
            return 3
        for line in lines:
            print(f"{type(line)}")
            print(f"{len(line)}, {line[0]}, {line[1]}")
            if  len(line) != 5: 
                print("fail in len")
                return 2 
            if line[0] != '+' and line[0] != '-':
                print("fail in sign")
                return 2
            if "43" in line[1:3]:
                includes_halt = True  
        if includes_halt == False:
            return 1
        return 0 
