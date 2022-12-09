from . import graphics

def collide_hitbox(
		x1: int, y1: int, width1: int, height1: int, 
		x2: int, y2: int, width2: int, height2: int) -> bool:
		
	if x1 < x2 < x1 + width1:
		return True
	elif y1 > y2 > y1 + height1:
		return True
	else:
		return False