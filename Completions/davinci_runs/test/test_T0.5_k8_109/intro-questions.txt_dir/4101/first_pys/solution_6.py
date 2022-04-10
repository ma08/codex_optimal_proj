

def solve(matrix):
    n = len(matrix)
    m = len(matrix[0])
    r = ''
    c = ''
    for i in range(n):
        if sum(matrix[i]) > m // 2:
            r += '1'
        else:
            r += '0'
    for j in range(m):
        if sum([matrix[i][j] for i in range(n)]) > n // 2:
            c += '1'
        else:
            c += '0'
    for i in range(n):
        for j in range(m):
            matrix[i][j] ^= int(r[i]) ^ int(c[j])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] > matrix[i][j - 1]:
                return 'NO'
    return 'YES\n' + r + '\n' + c


n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
print(solve(matrix))