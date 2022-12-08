from . import graphics

def rectangle(x, y, width, height, rgb, dest):
    r = graphics.Rectangle(graphics.Point(x, y), graphics.Point(x + width, y + height))
    r.setFill(graphics.color_rgb(rgb[0], rgb[1], rgb[2]))
    r.setOutline(graphics.color_rgb(rgb[0], rgb[1], rgb[2]))
    r.draw(dest.display)

def line(x, y, dest_x, dest_y, rgb, dest):
    r = graphics.Line(graphics.Point(x, y), graphics.Point(dest_x, dest_y))
    r.setFill(graphics.color_rgb(rgb[0], rgb[1], rgb[2]))
    r.setOutline(graphics.color_rgb(rgb[0], rgb[1], rgb[2]))
    r.draw(dest.display)

def image(x, y, image, dest):
    r = graphics.Image(graphics.Point(x, y), image).draw(dest.display)

def ellipsis(x, y, width, height, rgb, dest):
    r = graphics.Oval(graphics.Point(x, y), graphics.Point(x + width, y + height))
    r.setFill(graphics.color_rgb(rgb[0], rgb[1], rgb[2]))
    r.setOutline(graphics.color_rgb(rgb[0], rgb[1], rgb[2]))
    r.draw(dest.display)