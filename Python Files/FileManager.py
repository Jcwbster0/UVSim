import os
from tkinter import filedialog, messagebox

VALID_OPCODES = {"10", "010",
                 "11", "011",
                 "20", "020",
                 "21", "021",
                 "30", "030",
                 "31", "031",
                 "32", "032",
                 "33", "030",
                 "40", "040",
                 "41", "041",
                 "42", "042",
                 "43", "043"}

class FileManager:
    
    def __init__(self):
        return

    def openFile(self):
        filePath = self.promptForFile()
        defaultLines = []
        if not filePath or filePath[-4:] != ".txt":
            return (defaultLines,  "Error: .txt file expected")

        with open(filePath, "r") as file:
            lines = [line.rstrip("\n") for line in file.readlines()]
            lines = self.convertFile(lines)
            errCode = self.validateFile(lines)
            match errCode:
                case 0:
                    return (lines, os.path.basename(filePath))
                case 1:
                    return (defaultLines, "Error: no HALT(043) code")
                case 2:
                    return (defaultLines, "Error: invalid opcode")
                case 3:
                    return (defaultLines, "Error: memory exceeded 250 words.")

    def promptForFile(self):
       filePath = filedialog.askopenfilename(title="Choose a File", filetypes = [("Text Files", "*.txt")])
       return filePath

    def validateFile(self, lines):
        includes_halt = False

        if len(lines) > 250:
            return 3

        for line in lines:
            if len(line) != 7:
                return 2

            if line[0] != '+' and line[0] != '-':
                return 2

            digits = line[1:]
            if not digits.isdigit():
                return 2

            opcode = line[1:4]

            if opcode == "043":
                includes_halt = True

        if includes_halt == False:
            return 1

        return 0

    def convertFile(self, lines):
        convertedLines = []

        for line in lines:
            if len(line) == 5:
                sign = line[0]
                digits = line[1:]
                opcode = line[1:3]
                address = line[3:5]

                if opcode in VALID_OPCODES:
                    opcode = "0" + opcode
                    address = "0" + address
                    convertedLines.append(sign + opcode + address)
                else:
                    digits = "00" + digits
                    convertedLines.append(sign + digits)
            else:
                convertedLines.append(line)

        return convertedLines

    def saveFile(self, memory):
        file_path = filedialog.asksaveasfilename(
            initialfile="untitled.txt",
            defaultextension=".txt",
            filetypes=[
                ("Text Files", "*.txt"),
                ("All Files", "*.*")
            ]
        )
        
        if not file_path:
            return ("Save operation cancelled by user.", "error")
            
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                for line in memory:
                    line = line + "\n"
                    file.write(line)
            return (f"File successfully saved to: {os.path.basename(file_path)}", "write")
        except Exception as e:
            return (f"An error occurred while saving {e}", "error")

