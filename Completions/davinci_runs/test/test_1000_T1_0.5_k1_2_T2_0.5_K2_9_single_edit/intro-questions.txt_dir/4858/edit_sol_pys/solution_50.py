
M, N, C = input().split()
M = int(M)
N = int(N)
first = []
second = []
for i in range(M):
    first.append(list(input()))
for i in range(M):
    second.append(list(input()))
for i in range(M):
    for j in range(N):
        if first[i][j] != C:
            first[i][j] = '.'
        else:
            first[i][j] = 'X'
        if second[i][j] != C:
            second[i][j] = '.'
        else:
            second[i][j] = 'X'
for i in range(M):
    for j in range(N):
        if second[i][j] == 'X' and first[i][j] != 'X':
            second[i][j] = '^'
for i in range(M):
    for j in range(N):
        if second[i][j] == '^':
            second[i][j] = '.'
        if second[i][j] == 'X':
            second[i][j] = C
for i in range(M):
    print(''.join(second[i]))
print()
