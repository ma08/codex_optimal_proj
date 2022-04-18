import math

def decrypt(message):
    length = len(message)
    sqr = math.sqrt(length)
    if sqr == int(sqr):
        sqr = int(sqr)
        return decrypt_square(message, sqr)
    else:
        sqr = int(sqr)
        return decrypt_rectangle(message, sqr, sqr+1)

def decrypt_square(message, sqr):
    matrix = [['' for i in range(sqr)] for j in range(sqr)]
    for i in range(sqr):
        for j in range(sqr):
            matrix[i][j] = message[i*sqr + j]
    return ''.join([row[i] for i in range(sqr) for row in matrix])

def decrypt_rectangle(message, rows, cols):
    matrix = [['' for i in range(cols)] for j in range(rows)]
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = message[i*cols + j]
    return ''.join([row[i] for i in range(cols) for row in matrix])


message = input()
print(decrypt(message))
