import math

message = input("Enter your message: ")

length = len(message)

rows = math.sqrt(length)

columns = math.sqrt(length)

if rows.is_integer():
    rows = int(rows)
    columns = int(columns)
else:
    rows = math.floor(rows)
    columns = math.ceil(columns)

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
