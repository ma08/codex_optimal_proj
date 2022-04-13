
import math  # import math module

message = input() # take input

length = len(message)  # get length of input

rows = math.sqrt(length)  # get number of rows

columns = math.sqrt(length) # get number of columns

if rows.is_integer(): # check if rows is integer
    rows = int(rows)
    columns = int(columns)
else: # if not integer
    rows = math.floor(rows)
    columns = math.ceil(columns)

matrix = [] # create matrix

for i in range(0, rows): # add rows
    matrix.append([]) # add row
    for j in range(0, columns):
        matrix[i].append("0") # add column

for i in range(0, rows): # populate matrix
    for j in range(0, columns):
        if j + (i * columns) < length: # check if within length
            matrix[i][j] = message[j + (i * columns)] # populate matrix

output = ""

for j in range(0, columns):
    for i in range(0, rows):
        if matrix[i][j] != "0":
            output += matrix[i][j]

print(output)
