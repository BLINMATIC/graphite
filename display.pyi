import tkinter as tk
from . import commons

class Screen:
    def __init__(self, width: int, height: int, title: str) -> None:
        """Screen object. Takes in dimensions and a title."""

    def fill(self, rgb: commons.scalar3) -> None:
        """Fills the background."""

    def update(self) -> None:
        """Refreshes the screen."""