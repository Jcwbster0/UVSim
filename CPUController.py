import FileManager


class CPUController:
    def __init__(self, cpu, fileManager):
        self.cpu = cpu
        self.fileManager = fileManager

    def handleOpenFile(self):
        filePath = self.fileManager.promptForFile()

        if not filePath:
            return "Unable to Read File"

        return filePath
    
    def runProgramButtonPressed():
        #do the executions etc
        return

    def userInputButtonPressed():
        #read user input
        return
