from cairo import Rectangle
from manim import *

v_buff = 0.8
h_buff = 1.3

def newMatrix(matrix, i, j, k, l, scene):
    top_left = str(matrix[i][j])
    top_right = str(matrix[i][l])
    botttom_left = str(matrix[k][j])
    bottom_right = str(matrix[k][l])

    original = makeMatrix(matrix, lambda p, q: WHITE)
    original.shift(3 * LEFT)

    def colorCorners(p, q):
        if (p == i and q == j) or (p == k and q == l):
            return BLUE
        if (p == i and q == l) or (p == k and q == j):
            return YELLOW
        return WHITE
        
    colored = makeMatrix(matrix, colorCorners)
    colored.shift(3 * LEFT)

    column_width = (colored.width - 2 * MED_SMALL_BUFF) / len(matrix[0])
    row_height = (colored.height - 2 * MED_SMALL_BUFF) / len(matrix)

    # TODO this calculation is still a bit off for small rectangles
    r = Rectangle(height=row_height * (k - i + 1), width=column_width * (l - j + 1))
    r.align_to(colored.get_columns()[j], LEFT)
    r.align_to(colored.get_rows()[i], UP)
    r.apply_function_to_position(lambda coord: [coord[0] - 0.15, coord[1] + 0.1, coord[2]])

    example = MathTex(f"{top_left} + {bottom_right} \le {botttom_left} + {top_right}", substrings_to_isolate=[top_right, top_left, bottom_right, botttom_left])
    example.set_color_by_tex(top_left, BLUE)
    example.set_color_by_tex(bottom_right, BLUE)
    example.set_color_by_tex(top_right, YELLOW)
    example.set_color_by_tex(botttom_left, YELLOW)
    example.shift(RIGHT)
    example.shift(RIGHT)
    example.shift(RIGHT)

    scene.add(original)
    scene.play(Create(r))
    scene.remove(original)
    scene.add(colored)
    scene.wait(1)
    scene.add(example)

def makeMatrix(matrix, color_fn):
    texMatrix = []
    for p in range(0, len(matrix)):
        row = []
        for q in range(0, len(matrix[p])):
            row.append(Tex(str(matrix[p][q]), color=color_fn(p, q)))
        texMatrix.append(row)
    return MobjectMatrix(texMatrix)

