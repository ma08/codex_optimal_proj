

a, b = input().split()
N, M = len(b), len(a)

for i in range(M):
    for j in range(N):
        if a[j] == b[i]:
            print(b[i], end='')
        else:
            print('.', end='')
    print()
