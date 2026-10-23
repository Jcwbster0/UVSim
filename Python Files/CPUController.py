import FileManager
import tkinter as tk


class CPUController:
    def __init__(self, cpu, fileManager):
        self.cpu = cpu
        self.fileManager = fileManager
        self.output = None
        self.editor = None
        self.memory = []
        self.currentInput = ""
        self.requestForInput = False

    def handleOpenFile(self):
        lines, labelText = self.fileManager.openFile()
        length = len(lines)
        self.resetMemory()
        self.memory = lines + self.memory[length:]
        self.handleUpdateMemory(self.memory)
        return labelText

    def handleUpdateMemory(self, memory):
        self.editor.updateMemory(memory)

    def handleGetMemory(self):
        return self.editor.getMemory()

    def handleRunProgram(self, userInput=None):
        if userInput == None:
            self.memory = self.handleGetMemory()
        outputMsg = self.cpu.execute(self, userInput=userInput)
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
                    self.handleRunProgram(userInput=userInput)
                else:
                    raise ValueError
            except ValueError:
                self.pushToOutput(
                    "Invalid Input: enter an integer between -9999 and 9999.\n",
                    msgType="error",
                )

    def handleRead(self):
        self.requestForInput = True

    def handleWrite(self, output):
        self.pushToOutput(output, msgType="write")

    def setupEditor(self, fileEditorFrame):
        self.editor = fileEditorFrame

    def setupOutput(self, fileOutputFrame):
        self.output = fileOutputFrame

    def setupMemory(self):
        for i in range(100):
            self.memory.append("+0000")

    def resetMemory(self):
        self.cpu.reset()
        self.memory = []
        self.setupMemory()

    def setup(self, fileOutputFrame, fileEditorFrame):
        self.setupEditor(fileEditorFrame)
        self.setupOutput(fileOutputFrame)
        self.setupMemory()
        self.startupMessage()

    # Message tags:
    # - "write": Used for text that is meant to be more noticable such as the contents of the Write opcode
    # - "system": Used for things like writing opcodes to output. Smaller, less noticable
    # - "error": Used for error messages that are meant to grab the user's attention
    def pushToOutput(self, msg, msgType="write"):
        self.output.pushToOutput(msg, msgType)

    def startupMessage(self):
        message = r"""              __ _
 /\ /\/\   /\/ _(_)_ __ ___
/ / \ \ \ / /\ \| | '_ ` _ \
\ \_/ /\ V / _\ \ | | | | | |
 \___/  \_/  \__/_|_| |_| |_|"""
        message2 = "\n-----------------------------\n The Student Cpu Simulator\n-----------------------------\n"
        message3 = "Open a File and Select Run Program to get started!\n"
        message = message + message2 + message3
        self.pushToOutput(message)
