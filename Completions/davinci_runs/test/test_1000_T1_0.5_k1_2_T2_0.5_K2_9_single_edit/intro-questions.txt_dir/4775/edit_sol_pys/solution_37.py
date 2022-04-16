

a, b = input().split()
N, M = len(a), len(b)

for i in range(N):
    for j in range(M):
        if a[j] == b[i]:
            print(b[i], end='')
        else:
            print('.', end='')
    print()
