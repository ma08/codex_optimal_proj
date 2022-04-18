
message = input()

for n in range(1, len(message) + 1):
    if len(message) % n == 0:
        r = n
        c = int(len(message) / n)

matrix = [[0 for x in range(c)] for y in range(r)]

count = 0
for i in range(r):
    for j in range(c):
        matrix[i][j] = message[count]
        count += 1

for i in range(c):
    for j in range(r):
        print(matrix[j][i], end='')
    print()
