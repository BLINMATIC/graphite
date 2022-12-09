from . import graphics
import tkinter as tk
from typing import Tuple

class Screen:
	def __init__(self, icon: str, width: int, height: int, title: str) -> None:
		self.width = width
		self.height = height

		self.title = title

		self.icon = tk.PhotoImage(file = icon)
		self.display = graphics.GraphWin(icon, self.title, self.width, self.height, )
	
	def fill(self, rgb: Tuple[int, int, int]): 
		self.display.setBackground(graphics.color_rgb(rgb[0], rgb[1], rgb[2]))

	def get_width(self) -> int: 
		return self.width

	def get_height(self) -> int: 
		return self.height

	def get_title(self) -> str: 
		return self.title
	
	def update(self) -> None:
		self.display.master.wm_iconphoto(False, self.icon)
		self.display.update()
		
		for i in self.display.items[:]: 
			i.undraw()