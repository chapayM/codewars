# Given two different positions on a chess board, find the least number of moves it would take a knight
# to get from one to the other. The positions will be passed as two arguments in algebraic notation.
# For example, knight("a3", "b5") should return 1.
#
# The knight is not allowed to move off the board. The board is 8x8.
#
# For information on knight moves, see https://en.wikipedia.org/wiki/Knight_%28chess%29
#
# For information on algebraic notation, see https://en.wikipedia.org/wiki/Algebraic_notation_%28chess%29
#
# (Warning: many of the tests were generated randomly. If any do not work, the test cases will return the input,
# output, and expected output; please post them.)

# def knight(p1, p2):
#     vertical = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
#     gorizontal = ('1', '2', '3', '4', '5', '6', '7', '8')
#     pi, p2 = [[p1[0], p1[1], 0], ], list(p2)
#     for el in pi:
#         for i in [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]:
#             if 0 <= vertical.index(el[0])+i[0] <= 7 and 0 <= gorizontal.index(el[1])+i[1] <= 7:
#                 el_new = [vertical[vertical.index(el[0])+i[0]], gorizontal[gorizontal.index(el[1])+i[1]], el[2]+1]
#                 if el_new[0] == p2[0] and el_new[1] == p2[1]:
#                     return el_new[2]
#                 else:
#                     pi.append(el_new)


# def knight(p1, p2):
#     a, b = [('abcdefgh'.index(p[0]), int(p[1])) for p in [p1, p2]]
#     x, y = sorted((abs(a[0] - b[0]), abs(a[1] - b[1])))[::-1]
#
#     if (x, y) == (1, 0): return 3
#     if (x, y) == (2, 2) or ((x, y) == (1, 1) and any(p in ['a1', 'h1', 'a8', 'h8'] for p in [p1, p2])): return 4
#
#     delta = x - y
#
#     return delta - 2 * ((delta - y) // (3 if y > delta else 4))

def knight(p1, p2):
    # start here!

    mask = [[0, 3, 2, 3, 2, 3, 4, 5, ],
            [3, 2, 1, 2, 3, 4, 3, 4, ],
            [2, 1, 4, 3, 2, 3, 4, 5, ],
            [3, 2, 3, 2, 3, 4, 3, 4, ],
            [2, 3, 2, 3, 4, 3, 4, 5, ],
            [3, 4, 3, 4, 3, 4, 5, 4, ],
            [4, 3, 4, 3, 4, 5, 4, 5, ],
            [5, 4, 5, 4, 5, 4, 5, 6, ]]

    corner = ['a1', 'a8', 'h1', 'h8']

    dx = abs(ord(p1[0]) - ord(p2[0]))
    dy = abs(ord(p1[1]) - ord(p2[1]))

    if dx == 1 and dy == 1 and ((p1 in corner) or (p2 in corner)):
        return 4
    else:
        return mask[dx][dy]


print(knight('a1', 'f7'))
