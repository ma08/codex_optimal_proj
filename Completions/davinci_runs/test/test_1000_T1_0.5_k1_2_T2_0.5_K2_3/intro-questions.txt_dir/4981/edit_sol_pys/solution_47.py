N, M = map(int, input().split())
A = [input() for i in range(N)]
B = [input() for i in range(M)]

for i in range(N - M + 1):
    for j in range(N - M + 1):
        if A[i][j] == B[0][0]:
            match = True
            for k in range(M):
                for l in range(M):
                    if A[i+k][j+l] != B[k][l]:
                        match = False
            if match:
                print('Yes')
                exit()

print('No')
