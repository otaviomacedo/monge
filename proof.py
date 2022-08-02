from cairo import Rectangle
from lib.matrix import make_matrix

from manim import *

def implications(scene):
    general_matrix = make_matrix([
        [10, 17, 13, 28, 23],
        [17, 22, 16, 29, 23],
        [24, 28, 22, 34, 24],
        [11, 13, 6, 17, 7],
        [45, 44, 32, 37, 23],
        [36, 33, 19, 21, 6],
        [75, 66, 51, 53, 34]
    ], lambda p, q: WHITE)
    general_matrix.shift(3.6 * LEFT)

    general_hightlight = Rectangle(height=3.8, width=3.3)
    general_hightlight.shift(3.6 * LEFT)

    general_statement = Tex(r"Any $h\times w$ rectangle")
    general_statement.next_to(general_matrix, DOWN)

    special_matrix = make_matrix([
        [10, 17, 13, 28, 23],
        [17, 22, 16, 29, 23],
        [24, 28, 22, 34, 24],
        [11, 13, 6, 17, 7],
        [45, 44, 32, 37, 23],
        [36, 33, 19, 21, 6],
        [75, 66, 51, 53, 34]
    ], lambda p, q: WHITE)
    special_matrix.shift(3.6 * RIGHT)

    special_hightlight = Rectangle(height=1.4, width=2.05)
    special_hightlight.shift(2.95 * RIGHT)
    special_hightlight.shift(1.2 * UP)

    special_statement = Tex(r"Any $1\times 1$ rectangle")
    special_statement.next_to(special_matrix, DOWN)


    forward = MathTex(r"\Rightarrow")

    scene.add(general_matrix)
    scene.add(general_hightlight)
    scene.add(general_statement)

    scene.add(forward)

    scene.add(special_matrix)
    scene.add(special_hightlight)
    scene.add(special_statement)

def animated_implications(scene):
    numbers = [
        [10, 17, 13, 28, 23],
        [17, 22, 16, 29, 23],
        [24, 28, 22, 34, 24],
        [11, 13, 6, 17, 7],
        [45, 44, 32, 37, 23],
        [36, 33, 19, 21, 6],
        [75, 66, 51, 53, 34]]

    matrix = make_matrix(numbers, lambda p, q: WHITE)

    faded_matrix = make_matrix(numbers, lambda p, q: GRAY_D)

    highlight_1 = Rectangle(height=3.8, width=3.3, color=YELLOW)
    width_1 = Brace(highlight_1, UP, color=YELLOW)
    height_1 = Brace(highlight_1, LEFT, color=YELLOW)
    height_1_text = MathTex("h", color=YELLOW)
    height_1_text.next_to(height_1, LEFT)
    width_1_text = MathTex("w", color=YELLOW)
    width_1_text.next_to(width_1, UP)

    highlight_2 = Rectangle(height=1.37, width=5.8, color=YELLOW)
    highlight_2.align_to(highlight_1, UP)
    width_2 = Brace(highlight_2, UP, color=YELLOW)
    height_2 = Brace(highlight_2, LEFT, color=YELLOW)
    height_2_text = MathTex("h", color=YELLOW)
    height_2_text.next_to(height_2, LEFT)
    width_2_text = MathTex("w", color=YELLOW)
    width_2_text.next_to(width_2, UP)
    
    highlight_3 = Rectangle(height=3.8, width=2, color=YELLOW)
    highlight_3.align_to(highlight_2, RIGHT)
    highlight_3.shift(0.8 * UP)
    highlight_3.shift(0.05 * RIGHT)
    width_3 = Brace(highlight_3, UP, color=YELLOW)
    height_3 = Brace(highlight_3, LEFT, color=YELLOW)
    height_3_text = MathTex("h", color=YELLOW)
    height_3_text.next_to(height_3, LEFT)
    width_3_text = MathTex("w", color=YELLOW)
    width_3_text.next_to(width_3, UP)

    highlight_4 = Rectangle(height=1.4, width=2, color=YELLOW)
    highlight_4.align_to(highlight_3, UP)
    highlight_4.align_to(highlight_3, RIGHT)
    width_4 = Brace(highlight_4, UP, color=YELLOW)
    height_4 = Brace(highlight_4, LEFT, color=YELLOW)
    height_4_text = MathTex("h", color=YELLOW)
    height_4_text.next_to(height_4, LEFT)
    width_4_text = MathTex("w", color=YELLOW)
    width_4_text.next_to(width_4, UP)


    final_width_text = Tex("2", color=YELLOW)
    final_width_text.next_to(width_4, UP)
    final_height_text = Tex("2", color=YELLOW)
    final_height_text.next_to(height_4, LEFT)


    # Animation
    # -----------------------------------------------------------------

    scene.add(matrix)
    scene.wait(5.5)
    
    scene.play(*[
        Transform(matrix, faded_matrix),
        FadeIn(highlight_1),
        FadeIn(width_1),
        FadeIn(width_1_text),
        FadeIn(height_1),
        FadeIn(height_1_text),
    ])
    scene.wait(3)

    scene.play(*[
        Transform(highlight_1, highlight_2),
        Transform(width_1, width_2),
        Transform(height_1, height_2),
        Transform(width_1_text, width_1_text),
        Transform(height_1_text, height_2_text)
    ])
    
    scene.wait(3)

    scene.remove(highlight_1)
    scene.remove(width_1)
    scene.remove(height_1)
    scene.remove(width_1_text)
    scene.remove(height_1_text)

    scene.play(*[
        Transform(highlight_2, highlight_3),
        Transform(width_2, width_3),
        Transform(height_2, height_3),
        Transform(width_2_text, width_3_text),
        Transform(height_2_text, height_3_text)
    ])

    scene.wait(3)

    scene.remove(highlight_2)
    scene.remove(width_2)
    scene.remove(height_2)
    scene.remove(width_2_text)
    scene.remove(height_2_text)

    scene.play(*[
        Transform(highlight_3, highlight_4),
        Transform(width_3, width_4),
        Transform(height_3, height_4),
        Transform(width_3_text, width_4_text),
        Transform(height_3_text, height_4_text)
    ])

    scene.wait(1)

    scene.play(*[
        Transform(height_3_text, final_height_text),
        Transform(width_3_text, final_width_text)
    ])