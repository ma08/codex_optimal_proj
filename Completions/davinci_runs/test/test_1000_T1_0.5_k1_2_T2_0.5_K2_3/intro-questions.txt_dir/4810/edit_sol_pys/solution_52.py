
import math

def decrypt(message):
    length = len(message)
    max_rows = int(math.sqrt(length))
    rows = max_rows
    columns = max_rows
    if rows * columns < length:
        rows += 1

    matrix = [['' for x in range(columns)] for y in range(rows)]
    for i in range(length):
        matrix[i//columns][i%columns] = message[i]

    decrypted = []
    for i in range(length):
        decrypted.append(matrix[i//columns][i%columns])

    return ''.join(decrypted)


message = input()
print(decrypt(message))
