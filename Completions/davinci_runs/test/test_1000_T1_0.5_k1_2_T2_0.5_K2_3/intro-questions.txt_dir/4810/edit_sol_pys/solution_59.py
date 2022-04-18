# get message
import math
# get length of message
message = input()
# get rows
length = len(message)
# get columns
rows = math.sqrt(length)
# if rows is integer
columns = math.sqrt(length)

if rows.is_integer():
    rows = int(rows)
    columns = int(columns)
else:
    rows = math.floor(rows)
    columns = math.ceil(columns)
# matrix of message
matrix = []
# fill matrix with zeros
for i in range(0, rows):
    matrix.append([])
    for j in range(0, columns):
        matrix[i].append("0")
# fill matrix with message
for i in range(0, rows):
    for j in range(0, columns):
        if j + (i * columns) < length:
            matrix[i][j] = message[j + (i * columns)]
# output message
output = ""
# fill output message
for j in range(0, columns):
    for i in range(0, rows):
        if matrix[i][j] != "0":
            output += matrix[i][j]

print(output)
