from . import graphics
import tkinter as tk
from . import draw

class Screen:
    def __init__(self, icon, width=640, height=480, title="Graphite Window"):
        self.width = width
        self.height = height
        self.title = title
        self.icon = tk.PhotoImage(file = icon)

        self.display = graphics.GraphWin(icon, self.title, self.width, self.height, )

    def fill(self, rgb): self.display.setBackground(graphics.color_rgb(rgb[0], rgb[1], rgb[2]))
    def get_width(self): return self.width
    def get_height(self): return self.height
    def get_title(self): return self.title

    def update(self):
        self.display.update()
        self.display.master.wm_iconphoto(False, self.icon)
        for i in self.display.items[:]: i.undraw()