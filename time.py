import time


class Clock:
    def __init__(self): pass
    def tick(self, hz: int): time.sleep(1/hz)


def wait(ms: int): time.sleep(ms / 1000)