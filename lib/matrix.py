from cairo import Rectangle
from manim import *

v_buff = 0.8
h_buff = 1.3

def newMatrix(matrix, i, j, k, l, scene):
    for p in range(0, len(matrix)):
        row = matrix[p]
        for q in range(0, len(row)):
            color = WHITE
            if (p == i and q == j) or (p == k and q == l):
                color = BLUE
            if (p == i and q == l) or (p == k and q == j):
                color = YELLOW
            row[q] = Tex(str(row[q]), color=color)
        matrix[p] = row

    m = MobjectMatrix(matrix)
    m.shift(LEFT)
    m.shift(LEFT)
    m.shift(LEFT)
    scene.add(m)

    column_width = (m.width - 2 * MED_SMALL_BUFF) / len(matrix[0])
    row_height = (m.height - 2 * MED_SMALL_BUFF) / len(matrix)

    r = Rectangle(height=row_height * (k - i + 1), width=column_width * (l - j + 1))

    r.align_to(m.get_columns()[j], LEFT)
    r.align_to(m.get_rows()[i], UP)
    r.apply_function_to_position(lambda coord: [coord[0] - 0.15, coord[1] + 0.1, coord[2]])
    scene.add(r)
