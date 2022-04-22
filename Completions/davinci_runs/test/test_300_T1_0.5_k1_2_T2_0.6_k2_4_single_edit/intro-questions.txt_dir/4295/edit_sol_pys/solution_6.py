

N, K = map(int, input().split())

if K <= N:
    if N % K == 0:
        print(0)
    else:
        print(1)
