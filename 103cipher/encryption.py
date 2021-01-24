#!/usr/bin/env python3

import sys
import math

def convert_ascii_key(str):
    count = 0
    row = math.ceil(math.sqrt(len(str)))
    col = math.ceil(math.sqrt(len(str)))
    mat = [[0] * int(row) for y in range(col)]
    for i in range(row):
        j = 0
        for j in range(col):
            if (count < len(str)):
                mat[i][j] = ord(str[count])
            count += 1
    return mat

def convert_ascii_message(n, str):
    count = 0
    row = math.ceil(len(str) / n)
    col = n
    mat = [[0] * int(col) for y in range(row)]
    for i in range(row):
        for j in range(col):
            if (count < len(str)):
                mat[i][j] = ord(str[count])
            count += 1
    return mat

def mult_matrix(key, message):
    result = [[0] * len(message[0]) for y in range(len(message))]

    for i in range(len(message)):
        for j in range(len(message[0])):
            for k in range(len(message[0])):
                result[i][j] += key[k][j] * message[i][k]
    return result