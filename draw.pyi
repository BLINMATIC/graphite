import tkinter as tk
from . import commons
from .display import Screen


def line(dest: Screen, pos1: commons.scalar2, pos2: commons.scalar2, rgb: commons.scalar3) -> None:
    """Draws a line."""

def rectangle(dest: Screen, dimensions: commons.scalar4, rgb: commons.scalar3) -> None:
    """Draws a filled rectangle."""

def box(dest: Screen, dimensions: commons.scalar4, rgb: commons.scalar3) -> None:
    """Draws a hollow rectangle."""

def ellipsis(dest: Screen, dimensions: commons.scalar4, rgb: commons.scalar3) -> None:
    """Draws a filled ellipse."""

def hollow_ellipsis(dest: Screen, dimensions: commons.scalar4, rgb: commons.scalar3) -> None:
    """Draws a hollow ellipse."""