import FileManager


class CPUController:
    def __init__(self, cpu, fileManager):
        self.cpu = cpu
        self.fileManager = fileManager
        self.current_file

    def handleOpenFile(self):
        filePath = self.fileManager.promptForFile()

        if not filePath:
            return "Unable to Read File"
            
        filePath = fileManager.validate_file(filePath)

        return filePath
    
    def handleRunProgram():
        #do the executions etc
        return

    def handleUserInput():
        #read user input
        return
