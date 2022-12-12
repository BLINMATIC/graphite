import tkinter as tk
from . import commons


class Screen:
    def __init__(self, width: int, height: int, title: str):
        self.width = width
        self.height = height
        self.title = title

        self.root = tk.Tk()
        self.root.geometry(str(self.width) + "x" + str(self.height))
        self.root.resizable(False, False)
        self.root.title(self.title)

        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()

    def fill(self, rgb: commons.scalar3):
        self.canvas.create_rectangle(0, 0, self.width, self.height, fill=commons.rgb2hex(rgb), outline=commons.rgb2hex(rgb))

    def update(self):
        self.root.update()
        self.canvas.delete("all")