import math

def decrypt(message):
    length = len(message)
    max_rows = int(math.sqrt(length))
    rows = max_rows
    columns = max_rows
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


messages = input()
print(decrypt(messages))
