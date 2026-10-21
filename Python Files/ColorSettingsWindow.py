import tkinter as tk
from tkinter import ttk, colorchooser

class ColorSettingsWindow(tk.Toplevel):
    def __init__(self, parent, colorConfig):
        super().__init__(parent)

        self.parent = parent
        self.colorConfig = colorConfig

        self.title("Color Settings")
        self.geometry("350x275")
        self.resizable(False, False)

        self.primary = colorConfig.getPrimary()
        self.secondary = colorConfig.getSecondary()
        self.text = colorConfig.getText()

        self.configure(bg = self.primary)

        ttk.Label(
            self,
            text = "Configure UVSim Colors",
            font = ("Courier", 14, "bold")
        ).pack(pady = 10)

        # All the buttons in the Color Settings window
        ttk.Button(
            self,
            text = "Choose Primary Color",
            command = lambda: self.chooseColor("primary")
        ).pack(pady = 5)

        ttk.Button(
            self,
            text = "Choose Secondary Color",
            command = lambda: self.chooseColor("secondary")
        ).pack(pady = 5)

        ttk.Button(
            self,
            text = "Choose Text Color",
            command = lambda: self.chooseColor("text")
        ).pack(pady = 5)

        ttk.Button(
            self,
            text = "Reset Back to Default Colors",
            command = self.setDefaultColors
        ).pack(pady = 5)

        ttk.Button(
            self,
            text = "Apply Colors",
            command = self.applyColors
        ).pack(pady = 10)

    # Code for the color picker
    def chooseColor(self, colorType):
        currentColors = {
            "primary": self.primary,
            "secondary": self.secondary,
            "text": self.text
        }

        color = colorchooser.askcolor(
            color = currentColors[colorType],
            title = f"Choose {colorType.title()} Color",
            parent = self
        )[1]

        if color is not None:
            if colorType == "primary":
                self.primary = color
            elif colorType == "secondary":
                self.secondary = color
            elif colorType == "text":
                self.text = color

    # Resets colors back to the default UVU theming
    def setDefaultColors(self):
        self.colorConfig.setDefaultColors()

        self.primary = self.colorConfig.getPrimary()
        self.secondary = self.colorConfig.getSecondary()
        self.text = self.colorConfig.getText()

    # Changes the colors of the window
    def applyColors(self):
        self.colorConfig.updatePrimary(self.primary)
        self.colorConfig.updateSecondary(self.secondary)
        self.colorConfig.updateText(self.text)

        self.parent.applyColors()
        self.destroy()

