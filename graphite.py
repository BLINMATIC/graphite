from . import graphics
import time
import keyboard


class Screen:
    def __init__(self, width=640, height=480, title="Graphite Window"):
        self.width = width
        self.height = height
        self.title = title

        self.display = graphics.GraphWin(self.title, self.width, self.height, autoflush=False)

    def fill(self, r, g, b): self.display.setBackground(graphics.color_rgb(r, g, b))

    def update(self):
        self.display.update()
        for i in self.display.items[:]: i.undraw()


class _Time:
    class Clock:
        def __init__(self): pass
        def tick(self, hz=120): time.sleep(1/hz)

    def __init__(self): pass
    def sleep(self, ms): time.sleep(ms / 100)


class _Draw:
    def __init__(self): pass

    def rectangle(self, x, y, width, height, red, green, blue, dest):
        r = graphics.Rectangle(graphics.Point(x, y), graphics.Point(x + width, y + height))
        r.setFill(graphics.color_rgb(red, green, blue))
        r.setOutline(graphics.color_rgb(red, green, blue))
        r.draw(dest.display)

    def line(self, x, y, dest_x, dest_y, red, green, blue, dest):
        r = graphics.Line(graphics.Point(x, y), graphics.Point(dest_x, dest_y))
        r.setFill(graphics.color_rgb(red, green, blue))
        r.setOutline(graphics.color_rgb(red, green, blue))
        r.draw(dest.display)

    def image(self, x, y, image, dest):
        r = graphics.Image(graphics.Point(x, y), image).draw(dest.display)

    def ellipsis(self, x, y, width, height, red, green, blue, dest):
        r = graphics.Oval(graphics.Point(x, y), graphics.Point(x + width, y + height))
        r.setFill(graphics.color_rgb(red, green, blue))
        r.setOutline(graphics.color_rgb(red, green, blue))
        r.draw(dest.display)


class _Input:
    def __init__(self):
        self.x = 0
        self.y = 0

    def key(self, name):
        if keyboard.is_pressed(name): return 1
        else: return 0

    def mouse_pos(self, dest):
        dest.display.master.bind("<Motion>", self._motion)
        return self.x, self.y

    def _motion(self, event):
        self.x, self.y = event.x, event.y


Draw = _Draw()
Time = _Time()
Input = _Input()