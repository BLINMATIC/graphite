import keyboard
from .display import Screen

x = 0
y = 0

def key(name: str) -> bool:
	if keyboard.is_pressed(name): 
		return True
	else: 
		return False

def mouse_pos(dest: Screen):
	global x, y

	dest.display.master.bind("<Motion>", _motion)
	return x, y

def _motion(event):
	global x, y
	
	x, y = event.x, event.y
	return x, y