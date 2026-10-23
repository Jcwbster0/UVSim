import tkinter as tk
from tkinter import ttk
import UserInputFrame
import FileOutputFrame
import FileEditorFrame


class MainWindow(tk.Tk):

    def __init__(self, title, size, controller, colorConfig):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])
        self.windowTitle = title
        self.controller = controller
        self.colorConfig = colorConfig
        self.configure(bg=self.colorConfig.getPrimary())

        # Disable resizing
        self.resizable(False, False)
        # initialize ui widgets here

        self.userInputFrame = UserInputFrame.UserInputFrame(self, self.colorConfig)
        self.fileOutputFrame = FileOutputFrame.FileOutputFrame(self, self.colorConfig)
        self.fileEditorFrame = FileEditorFrame.FileEditorFrame(self)

        self.controller.setup(self.fileOutputFrame, self.fileEditorFrame)

        self.mainloop()

    # Updates the colors of the Main Window
    def applyColors(self):
        self.configure(bg=self.colorConfig.getPrimary())

        style = ttk.Style()
        style.configure("Custom.TFrame", background=self.colorConfig.getPrimary())
        style.configure(
            "Custom.TButton",
            background=self.colorConfig.getSecondary(),
            foreground=self.colorConfig.getText(),
        )
        style.configure(
            "Custom.TLabel",
            background=self.colorConfig.getPrimary(),
            foreground=self.colorConfig.getText(),
        )

        output = self.fileOutputFrame.outputFrame

        output.configure(
            bg=self.colorConfig.getSecondary(), fg=self.colorConfig.getText()
        )

        output.tag_config("write", foreground=self.colorConfig.getText())

        output.tag_config("system", foreground=self.colorConfig.getPrimary())

