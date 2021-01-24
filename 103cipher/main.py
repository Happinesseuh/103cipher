#!/usr/bin/env python3

import sys
import math
from encryption import *
from decryption import *

def print_key(matrix):
    print("Key matrix:")
    for i in range (len(matrix)):
        for j in range (len(matrix[i])):
            if (j < len(matrix[i]) - 1):
                print(round(matrix[i][j], 3), end = '\t')
            else:
                print(round(matrix[i][j], 3), end = '')
        print()
    print()

def print_help():
    print("USAGE")
    print("\t./103cipher message key flag\n")
    print("DESCRIPTION")
    print("\tmessage\ta message, made of ASCII characters")
    print("\tkey\tthe encryption key, made of ASCII characters")
    print("\tflag\t0 for the message to be encrypted, 1 to be decrypted")
    exit (84)

def print_encrypted(result):
    print("Encrypted message:")
    for i in range (len(result)):
        for j in range (len(result[i])):
            if (i == len(result) - 1 and j == len(result[i]) - 1):
                print(result[i][j], end = '')
            else:
                print(result[i][j], end = ' ')
        if (i < len(result) - 1):
            print(end = '')
        else:
            print()

def main():
    if (len(sys.argv) == 2 and sys.argv[1] == "-h"):
        print_help()
    elif (len(sys.argv) != 4 or (sys.argv[3] != "1" and sys.argv[3][0] != "0")):
        exit (84)
    if (sys.argv[3] == "0"):
        key = convert_ascii_key(sys.argv[2])
        n = len(key)
        message = convert_ascii_message(n, sys.argv[1])
        result = mult_matrix(key, message)
        print_key(key)
        print_encrypted(result)           
    elif (sys.argv[3] == "1"):
        key = convert_ascii_key(sys.argv[2])
        n = len(key)
        message = recup_message(n, sys.argv[1])
        if (len(key) == 1):
            reverse = key
            reverse[0][0] = 1/reverse[0][0]
        elif (len(key) == 2):
            reverse = transpose(reverse_two_by_two(key))
        elif (len(key) == 3):
            reverse = transpose(reverse_three_by_three(key))
        print_key(reverse)
        print_decrypted(result)
main()
