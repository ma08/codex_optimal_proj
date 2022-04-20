
# N, K = map(int, input().split())
N, K = 7, 4

if N % K == 0:
    print(0)
else:
    print(min(N % K, K - N % K))
