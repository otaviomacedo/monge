from tkinter import RIGHT
from lib.matrix import newMatrix
from manim import *


class Playground(Scene):
    def construct(self):

        foo = newMatrix([
            [10, 17, 13, 28, 23],
            [17, 22, 16, 29, 23],
            [24, 28, 22, 34, 24],
            [11, 13, 6, 17, 7],
            [45, 44, 32, 37, 23],
            [36, 33, 19, 21, 6],
            [75, 66, 51, 53, 34]
        ], 0, 0, 1, 1, self)


        self.wait(10)

