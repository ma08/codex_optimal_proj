

N, M = map(int, input().split())
if N % 2 == 0:
    print(N * M // 2)
else:
    print(N * M // 2 + M)
