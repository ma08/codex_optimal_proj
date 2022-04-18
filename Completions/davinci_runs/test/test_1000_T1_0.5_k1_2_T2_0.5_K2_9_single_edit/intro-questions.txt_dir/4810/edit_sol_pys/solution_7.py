#!/usr/bin/env python3

import math

def decrypt(message):
    length = len(message)
    sqrt = math.sqrt(length)
    if sqrt == int(sqrt): # is perfect sqrt
        sqrt = int(sqrt) 
        return decrypt_square(message, sqrt)
    else:
        rows = int(sqrt)
        cols = rows + 1
        return decrypt_rectangle(message, rows, cols)

def decrypt_square(message, sqrt):
    matrix = [['' for i in range(sqrt)] for j in range(sqrt)]
    for i in range(sqrt):
        for j in range(sqrt):
            matrix[i][j] = message[i*sqrt + j]
    return ''.join([row[i] for i in range(sqrt) for row in matrix])

def decrypt_rectangle(message, rows, cols):
    matrix = [['' for i in range(cols)] for j in range(rows)]
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = message[i*cols + j]
    return ''.join([row[i] for i in range(cols) for row in matrix])


message = input()
print(decrypt(message))
