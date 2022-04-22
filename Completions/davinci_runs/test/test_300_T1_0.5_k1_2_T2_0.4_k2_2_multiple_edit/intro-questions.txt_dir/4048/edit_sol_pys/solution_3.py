import random

n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

matrix = []

for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(random.randint(0, 100))

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=" ")
    print()
