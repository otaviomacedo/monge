from email.mime import base
from manim import *

def induction(scene):
    base_case = MathTex("A[i, j] + A[i + 1, j + 1] \le A[i, j + 1] + A[i + 1, j]")
    scene.add(base_case)