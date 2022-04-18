import math


def decrypt(message):
    length = len(message)
    max_rows = int(math.sqrt(length))
    columns = max_rows+1
    rows = max_rows+1
    if rows * columns < length:
        rows += 1

    matrix = [['' for x in range(columns)] for y in range(rows)]
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = message[i * columns + j]

    decrypted = []
    for j in range(columns):
        for i in range(rows):
            decrypted.append(matrix[i][j])

    return ''.join(decrypted)


message = input()
print(decrypt(message))
