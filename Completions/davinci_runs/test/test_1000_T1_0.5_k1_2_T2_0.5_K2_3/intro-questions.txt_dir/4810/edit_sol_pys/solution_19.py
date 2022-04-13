
import math

def encrypt(message):
    length = len(message)
    sqrt_length = math.sqrt(length)
    if sqrt_length == int(sqrt_length):
        sqrt_length = int(sqrt_length)
        return encrypt_square(message, sqrt_length)
    else:
        sqrt_length = int(sqrt_length)
        return encrypt_rectangle(message, sqrt_length, sqrt_length+1)

def encrypt_square(message, sqrt):
    matrix = [['' for i in range(sqrt)] for j in range(sqrt)]
    for i in range(sqrt):
        for j in range(sqrt):
            matrix[i][j] = message[i*sqrt + j]
    return ''.join([row[i] for i in range(sqrt) for row in matrix])

def encrypt_rectangle(message, rows, cols):
    matrix = [['' for i in range(cols)] for j in range(rows)]
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = message[i*cols + j]
    return ''.join([row[i] for i in range(cols) for row in matrix])


message = input()
print(encrypt(message))
