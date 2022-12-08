import keyboard

x = 0
y = 0

def key(name):
    if keyboard.is_pressed(name): return 1
    else: return 0

def mouse_pos(dest):
    global x, y
    dest.display.master.bind("<Motion>", _motion)
    return x, y

def _motion(event):
    global x, y
    x, y = event.x, event.y
    return x, y