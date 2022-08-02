from cairo import Rectangle
from manim import *

v_buff = 0.8
h_buff = 1.3

def animate(matrix, rectangles, scene):
    original = make_matrix(matrix, lambda p, q: WHITE)
    original.shift(3 * LEFT)

    column_width = (original.width - 2 * MED_SMALL_BUFF) / len(matrix[0])
    row_height = (original.height - 2 * MED_SMALL_BUFF) / len(matrix)

    scene.add(original)

    for rect in rectangles:
        i = rect[0]
        j = rect[1]
        k = rect[2]
        l = rect[3]

        # TODO this calculation is still a bit off for small rectangles
        r = Rectangle(height=row_height * (k - i + 1), width=column_width * (l - j + 1))
        r.align_to(original.get_columns()[j], LEFT)
        r.align_to(original.get_rows()[i], UP)
        r.apply_function_to_position(lambda coord: [coord[0] - 0.15, coord[1] + 0.1, coord[2]])

        top_left = str(matrix[i][j])
        top_right = str(matrix[i][l])
        botttom_left = str(matrix[k][j])
        bottom_right = str(matrix[k][l])

        def colorCorners(p, q):
            if (p == i and q == j) or (p == k and q == l):
                return BLUE
            if (p == i and q == l) or (p == k and q == j):
                return YELLOW
            return WHITE
        
        colored = make_matrix(matrix, colorCorners)
        colored.shift(3 * LEFT)

        example = MathTex(f"{top_left} + {bottom_right} \le {botttom_left} + {top_right}", substrings_to_isolate=[top_right, top_left, bottom_right, botttom_left])
        example.set_color_by_tex(top_left, BLUE)
        example.set_color_by_tex(bottom_right, BLUE)
        example.set_color_by_tex(top_right, YELLOW)
        example.set_color_by_tex(botttom_left, YELLOW)
        example.shift(RIGHT)
        example.shift(RIGHT)
        example.shift(RIGHT)

        scene.play(Create(r))
        scene.add(colored)
        scene.wait(1)
        scene.add(example)
        scene.wait(5)
        scene.remove(colored)
        scene.remove(example)
        scene.remove(r)

def make_matrix(matrix, color_fn):
    texMatrix = []
    for p in range(0, len(matrix)):
        row = []
        for q in range(0, len(matrix[p])):
            row.append(Tex(str(matrix[p][q]), color=color_fn(p, q)))
        texMatrix.append(row)
    return MobjectMatrix(texMatrix)

