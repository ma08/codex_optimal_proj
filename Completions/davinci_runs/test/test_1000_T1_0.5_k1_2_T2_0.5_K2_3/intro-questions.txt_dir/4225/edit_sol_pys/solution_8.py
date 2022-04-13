

A, B, C, K = map(int, input().split())
# A, B, C, K = 2, 2, 2, 100

for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            if i + j + k == K:
                print(i, j, k)
                exit()

print(-1, -1, -1)
