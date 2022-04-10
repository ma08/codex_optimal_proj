

n = int(input())
numbers = list(map(int, input().split()))

if n == 1:
    print('YES') 
    print(numbers[0])
    exit()

if len(numbers) != n ** 2:
    print('NO')
    exit()

numbers.sort()

if numbers[0] != numbers[n - 1] or numbers[n - 1] != numbers[2 * n - 2] or numbers[2 * n - 2] != numbers[3 * n - 3]:
    print('NO')
    exit()

if len(set(numbers)) == 1:
    print('YES')
    for i in range(n):
        for j in range(n):
            print(numbers[0], end=' ')
        print()
    exit()

matrix = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    matrix[i][i] = numbers[i]
    matrix[i][n - 1 - i] = numbers[i]

if n % 2 == 1:
    for i in range(n // 2 + 1, n):
        for j in range(n // 2 + 1, n):
            matrix[i][j] = numbers[n + i - n // 2 - 1 + j - n // 2 - 1]
            matrix[n - 1 - i][n - 1 - j] = matrix[i][j]
            matrix[i][n - 1 - j] = matrix[n - 1 - i][j] = matrix[j][i] = numbers[n + i - n // 2 - 1 + j - n // 2 - 1 + n // 2]
            matrix[n - 1 - i][j] = matrix[j][n - 1 - i] = matrix[n - 1 - j][i] = matrix[n - 1 - j][n - 1 - i] = numbers[n + i - n // 2 - 1 + j - n // 2 - 1 + n // 2]

# print('\n'.join([' '.join([str(i) for i in row]) for row in matrix]))

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 0:
            print('NO')
            exit()

if len(set([item for sublist in matrix for item in sublist])) != len(numbers):
    print('NO')
    exit()

print('YES')
print('\n'.join([' '.join([str(i) for i in row]) for row in matrix]))
