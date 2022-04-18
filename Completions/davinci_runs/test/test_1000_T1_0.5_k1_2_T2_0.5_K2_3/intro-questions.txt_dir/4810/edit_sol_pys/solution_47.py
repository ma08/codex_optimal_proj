
# This is a program to encrypt a message
# This loop finds the smallest possible square matrix
message = input()

r = int(input())
c = int(len(message) / r)

matrix = [[0 for x in range(r)] for y in range(c)]

count = 0
for i in range(c):
    for j in range(r):
        matrix[i][j] = message[count]
        count += 1

for i in range(r):
    for j in range(c):
        print(matrix[j][i], end="")
    print()
