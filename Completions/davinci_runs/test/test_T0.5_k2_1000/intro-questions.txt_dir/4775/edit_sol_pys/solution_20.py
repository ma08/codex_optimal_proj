
a = input()
b = input()
N = len(a)
M = len(b)

for i in range(M):
    for j in range(N):
        if a[j] == b[i] and i == j:
            print('.', end='')
        else:
            print(b[i], end=' ')
    print()
