from . import graphics
import time

def wait_precise(ms: int) -> None: 
	time.sleep(ms / 1000)

def wait(ms: int) -> None: 
	time.sleep(ms // 1000)

class Clock:
	def __init__(self) -> None: 
		pass

	def tick(self, hz: int) -> None: 
		time.sleep(1 / hz)