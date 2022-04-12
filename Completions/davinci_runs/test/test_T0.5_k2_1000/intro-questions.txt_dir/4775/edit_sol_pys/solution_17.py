a, b = input().split()
N, M = len(a), len(b)

for i in range(N):
    for j in range(M):
        if a[i] == b[j]:
            print(b[j], end='')
        else:
            print('.', end='')
    print()
