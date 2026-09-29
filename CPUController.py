import FileManager
import tkinter as tk


class CPUController:
    def __init__(self, cpu, fileManager):
        self.cpu = cpu
        self.fileManager = fileManager
        self.output = None
        self.memory = []
        self.currentInput = ""
        self.requestForInput = False

    def handleOpenFile(self):
        lines, labelText = self.fileManager.openFile()
        length = len(lines)
        self.memory = lines + self.memory[length:]
        print(self.memory)
        self.cpu.resetProgramCounter()
        return labelText
    
    def handleRunProgram(self, userInput = None):
        outputMsg = self.cpu.execute(self, userInput = userInput)
        if outputMsg is not None:
            self.pushToOutput(outputMsg)

    def handleUserInput(self, userInput):
        if self.requestForInput == True:
            try: 
                input = int(userInput)
                if input >= -9999 and input <= 9999:
                    requestForInput = False
                    self.pushToOutput(f"Input Accepted: {userInput}\n")
                    
                    self.currentInput = userInput
                    self.handleRunProgram(userInput = userInput)
                else:
                    raise ValueError
            except ValueError:
                self.pushToOutput("Invalid Input: enter an integer between -9999 and 9999.\n")              
            
    def handleRead(self):
        self.requestForInput = True

    def handleWrite(self, output):
        self.pushToOutput(output)

    def setupOutput(self, fileOutputFrame):
        self.output = fileOutputFrame

    def setupMemory(self):
        for i in range(100):
            self.memory.append("+0000")

    def setup(self, fileOutputFrame):
        self.setupOutput(fileOutputFrame)
        self.setupMemory()

    def pushToOutput(self, msg):
        self.output.pushToOutput(msg)
