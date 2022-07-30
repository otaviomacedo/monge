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
        ], 0, 0, 3, 4, self)

        example = MathTex(r"28 + 23 \le 44 + 24", substrings_to_isolate=["28", "23", "44", "24"])
        example.set_color_by_tex("28", BLUE)
        example.set_color_by_tex("23", BLUE)
        example.set_color_by_tex("44", YELLOW)
        example.set_color_by_tex("24", YELLOW)


        example.shift(RIGHT)
        example.shift(RIGHT)
        example.shift(RIGHT)
        self.add(example)

        self.wait(10)

