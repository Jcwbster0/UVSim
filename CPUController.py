import FileManager
import tkinter as tk


class CPUController:
    def __init__(self, cpu, fileManager):
        self.cpu = cpu
        self.fileManager = fileManager
        self.currentFile = ""
        self.currentInput = ""
        self.requestForInput = True

    def handleOpenFile(self):
        lines, labelText = self.fileManager.openFile()
        self.currentFile = lines
        return labelText
    
    def handleRunProgram():
        #do the executions etc
        return

    def handleUserInput(self, userInput, fileOutputFrame):
        if self.requestForInput == True:
            try: 
                input = int(userInput)
                if input >= -9999 and input <= 9999:
                    requestForInput = False
                    self.pushToOutput(fileOutputFrame, f"Input Accepted: {userInput}\n")
                    
                    self.currentInput = userInput
                    print(self.currentInput)
                    #self.cpu.execute()
                else:
                    raise ValueError
            except ValueError:
                self.pushToOutput(fileOutputFrame, "Invalid Input: enter an integer between -9999 and 9999.\n")              
            

    def pushToOutput(self, fileOutputFrame, msg):
        fileOutputFrame.normalState()
        fileOutputFrame.outputFrame.insert(tk.END, msg) 
        fileOutputFrame.disabledState()
         
