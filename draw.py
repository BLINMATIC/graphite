import tkinter as tk
from . import commons


def line(dest, pos1, pos2, rgb):
    dest.canvas.create_line(pos1[0], pos1[1], pos2[0], pos2[1], fill=commons.rgb2hex(rgb))


def rectangle(dest, dimensions, rgb):
    dest.canvas.create_rectangle(dimensions[0], dimensions[1], dimensions[0] + dimensions[2], dimensions[1] + dimensions[3], fill=commons.rgb2hex(rgb), outline=commons.rgb2hex(rgb))


def box(dest, dimensions, rgb):
    dest.canvas.create_rectangle(dimensions[0], dimensions[1], dimensions[0] + dimensions[2], dimensions[1] + dimensions[3], outline=commons.rgb2hex(rgb))


def ellipsis(dest, dimensions, rgb):
    dest.canvas.create_oval(dimensions[0], dimensions[1], dimensions[0] + dimensions[2], dimensions[1] + dimensions[3], fill=commons.rgb2hex(rgb), outline=commons.rgb2hex(rgb))


def hollow_ellipsis(dest, dimensions, rgb):
    dest.canvas.create_oval(dimensions[0], dimensions[1], dimensions[0] + dimensions[2], dimensions[1] + dimensions[3], outline=commons.rgb2hex(rgb))

