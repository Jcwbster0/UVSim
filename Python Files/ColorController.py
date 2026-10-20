from pathlib import Path

projectDirectory = Path(__file__).parent
colorPath = projectDirectory / "ColorSettings.txt"

class ColorController:
    def __init__(self):
        self.config = self.readConfigFile()
        self.primary = self.config[0]
        self.secondary = self.config[1]
        self.text = self.config[2]

    def setDefaultColors(self):
        self.updatePrimary("#4C721D")
        self.updateSecondary("#FFFFFF")
        self.updateText("#000000")

    def updatePrimary(self, userInput):
        self.primary = userInput
        with open(colorPath, "r") as file:
            data = file.readlines()

        data[0] = f'primary="{userInput}"\n'

        with open(colorPath, "w") as file:
            file.writelines(data)
        
    def updateSecondary(self, userInput):
        self.secondary = userInput
        with open(colorPath, "r") as file:
            data = file.readlines()

        data[1] = f'secondary="{userInput}"\n'

        with open(colorPath, "w") as file:
            file.writelines(data)

    def updateText(self, userInput):
        self.text = userInput
        with open(colorPath, "r") as file:
            data = file.readlines()

        data[2] = f'text="{userInput}"\n'

        with open(colorPath, "w") as file:
            file.writelines(data)

    def getPrimary(self):
        return self.primary

    def getSecondary(self):
        return self.secondary

    def getText(self):
        return self.text

    def readConfigFile(self):
        y = []
        with open (colorPath, "r") as file:
            content = file.readlines()
            for x in content:
                x = x.rstrip()
                y.append(x[-8:-1])
        return y
    