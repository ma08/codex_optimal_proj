import math
message = input().strip()
length = len(message)
rows = math.floor(math.sqrt(length))
columns = math.ceil(math.sqrt(length))

matrix = []
for i in range(0, rows):
    matrix.append([])
    for j in range(0, columns):
        matrix[i].append("0")
for i in range(0, rows):
    for j in range(0, columns):
        if j + (i * columns) < length:
            matrix[i][j] = message[j + (i * columns)]
output = ""
for j in range(0, columns):
    for i in range(0, rows):
        if matrix[i][j] != "0":
            output += matrix[i][j]
print(output)
