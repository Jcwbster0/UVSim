import FileManager


class CPUController:
    def __init__(self, cpu, fileManager):
        self.cpu = cpu
        self.fileManager = fileManager
        self.currentFile
        self.currentInput
        self.requestForInput

    def handleOpenFile(self):
        lines, labelText = self.fileManager.openFile()
        self.currentFile = lines
        return labelText
    
    def handleRunProgram():
        #do the executions etc
        return

    def handleUserInput(userInput, outputFrame):
        if requestForInput = True:
            try: 
                input = int(userInput)
                requestForInput = False
                self.pushToOutput(outputFrame, f"Input Accepted: {userInput}")
                self.cpu.execute()
            except ValueError:
                self.pushToOutput(outputFrame, "Invalid Input: enter a positive integer between -9999 and 9999.")              
            

    def pushToOutput(outputFrame, msg):
        outputFrame.insert("end", msg) 
         
