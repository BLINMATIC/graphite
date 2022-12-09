from . import graphics
from . import display
from typing import Tuple

def rectangle(x: int, y: int, width: int, height: int, rgb: Tuple[int, int, int], dest: display.Screen) -> None:
	r = graphics.Rectangle(graphics.Point(x, y), graphics.Point(x + width, y + height))

	r.setFill(graphics.color_rgb(rgb[0], rgb[1], rgb[2]))
	r.setOutline(graphics.color_rgb(rgb[0], rgb[1], rgb[2]))

	r.draw(dest.display)

def line(x: int, y: int, dest_x: int, dest_y: int, rgb: Tuple[int, int, int], dest: display.Screen) -> None:
	r = graphics.Line(graphics.Point(x, y), graphics.Point(dest_x, dest_y))

	r.setFill(graphics.color_rgb(rgb[0], rgb[1], rgb[2]))
	r.setOutline(graphics.color_rgb(rgb[0], rgb[1], rgb[2]))

	r.draw(dest.display)

def _image(x: int, y: int, image: str, dest: display.Screen) -> None:
	# This is used for the Sprite libary
	r = graphics.Image(graphics.Point(x, y), image).draw(dest)

def image(x: int, y: int, image: str, dest: display.Screen) -> None:
	r = graphics.Image(graphics.Point(x, y), image).draw(dest.display)

def ellipsis(x: int, y: int, width: int, height: int, rgb: Tuple[int, int, int], dest: display.Screen) -> None:
	r = graphics.Oval(graphics.Point(x, y), graphics.Point(x + width, y + height))

	r.setFill(graphics.color_rgb(rgb[0], rgb[1], rgb[2]))
	r.setOutline(graphics.color_rgb(rgb[0], rgb[1], rgb[2]))

	r.draw(dest.display)

class Sprite:
	def __init__(self, x: int, y: int, image: str, dest: display.Screen) -> None:
		self.x = x
		self.y = y

		self.image = image
		self.dest = dest

	def draw(self) -> None:
		_image(self.x, self.y, self.image, self.dest.display)