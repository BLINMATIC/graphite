from . import graphics
import time

def wait_precise(ms): time.sleep(ms / 1000)
def wait(ms): time.sleep(ms // 1000)

class Clock:
    def __init__(self): pass
    def tick(self, hz): time.sleep(1 / hz)