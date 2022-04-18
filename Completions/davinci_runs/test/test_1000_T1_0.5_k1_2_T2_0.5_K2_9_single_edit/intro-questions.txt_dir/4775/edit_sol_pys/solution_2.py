
a, b = input().split()
N, M = len(a), len(b)
for i in range(M):
    for j in range(N):
        if a[j] == b[i]:
            print(b[i], end='')
        else:
            print('.', end='')
    print()
