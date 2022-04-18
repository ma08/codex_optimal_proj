import math



def decrypt(message, columns):
    length = len(message)
    rows = int(math.ceil(length / columns))
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
