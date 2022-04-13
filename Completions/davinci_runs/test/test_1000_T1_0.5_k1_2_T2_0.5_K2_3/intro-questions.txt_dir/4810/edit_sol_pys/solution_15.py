

message = input()  # input message

for n in range(1, len(message) + 1):  # finding the number of rows and columns
    if len(message) % n == 0:  # checking if the number of rows is a factor of the number of characters
        r = n  # number of rows
        c = int(len(message) / n)  # number of columns

matrix = [[0 for x in range(c)] for y in range(r)]  # creating a matrix

count = 0
for i in range(r):
    for j in range(c):
        matrix[i][j] = message[count]
        count += 1

for i in range(c):
    for j in range(r):
        print(matrix[j][i], end=" ")
    print()
