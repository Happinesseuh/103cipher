
#!/usr/bin/env python3

import math

def transpose(matrix):
    result = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))]
    for i in range (len(matrix[0])):
        for j in range (len(matrix)):
            result[i][j] = matrix[j][i]
    return result

def det_two_by_two(matrix):
    a = matrix[0][0]
    d = matrix[1][1]
    c = matrix[1][0]
    b = matrix[0][1]
    det = (a * d) - (b * c)
    return det

def reverse_two_by_two(matrix):
    det = det_two_by_two(matrix)
    if (det == 0):
        return 84
    matrix[1][0] = det * (-matrix[1][0])
    matrix[1][0] = det * (-matrix[0][1])
    matrix[1][1] *= det
    matrix[0][0] *= det
    return matrix

def cofactors_three_by_three(matrix, i, j):
    stock = 0
    col = 0
    row = 0
    result = [[0 for x in range(2)] for y in range(2)]

    for a in range(3):
        for b in range(3):
            if (a != i and b != j):
                stock = matrix[a][b]
                result[row][col] = stock
                col += 1
                if (col == 2):
                    row += 1
                    col = 0
    det = det_two_by_two(result)
    if (det == 0):
        return 84
    sign =  math.pow(-1, i + j)
    cofactors = sign * det
    return (cofactors)

def range_cofactors_in_matrix(matrix):
    result = [[0 for x in range(3)] for y in range(3)]
    for i in range(3):
        for j in range(3):
            stock = cofactors_three_by_three(matrix, i, j)
            result[i][j] = stock
    return result

def det_three_by_three(matrix):
    result = ((matrix[0][0] * cofactors_three_by_three(matrix, 0, 0)) + (matrix[0][1] *
    cofactors_three_by_three(matrix, 0, 1)) + (matrix[0][2] *
    cofactors_three_by_three(matrix, 0, 2)))
    if (result == 0):
        return 84
    return result

def reverse_three_by_three(matrix):
    tab = range_cofactors_in_matrix(matrix)
    result = [[0 for x in range(3)] for y in range(3)]
    for i in range(3):
        for j in range(3):
            result[i][j] = (1/det_three_by_three(matrix)) * tab[i][j]
            if (round(result[i][j], 3) == -0.000):
                result[i][j] = 0.0
    return result

def recup_message(n, str):
    i = 0
    j = 0
    tab = [int(i) for i in str.split() if i.isdigit()]
    size = len(tab) / n
    matrix = [[0] * int(n) for i in range(int(size + 1))]
    for k in range(len(tab)):
        matrix[i][j] = tab[k]
        j += 1
        if (j == n):
            i += 1
            j = 0
    return matrix

def print_decrypted(result):
    print("Decrypted message:")
    for i in range(len(result)):
        for j in range(len(result[i])):
            c = (chr(round(result[i][j])))
            if (c.isprintable()):
                print(c)