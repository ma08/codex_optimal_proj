
a, b = input().split()
N, M = len(a), len(b)

if N >= M:
    for i in range(M):
        for j in range(N):
            if a[j] == b[i]:
                print(b[i], end='')
            else:
                print('.', end='')
        print()
else:
    for i in range(N):
        for j in range(M):
            if a[i] == b[j]:
                print(a[i], end='')
            else:
                print('.', end='')
        print()
