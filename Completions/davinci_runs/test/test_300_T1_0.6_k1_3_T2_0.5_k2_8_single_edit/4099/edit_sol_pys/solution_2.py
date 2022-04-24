

N, M = map(int, input().split())
A = list(map(int, input().split()))

K = M * N
S = sum(A)
x = K - S

if x < 0:
    print(-1)
elif x > K:
    print(-1)
else:
    print(x)
