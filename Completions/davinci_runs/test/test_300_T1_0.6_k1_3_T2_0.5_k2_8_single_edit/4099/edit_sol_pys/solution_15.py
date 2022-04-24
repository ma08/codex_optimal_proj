

# M * N = S + x
# x = M * N - S = (M - S / N) * N

N, K, M = map(int, input().split())
A = list(map(int, input().split()))

S = sum(A)
x = (M * N - S) // N

if x < 0:
    print(-1)
elif x > K:
    print(-1)
else:
    print(x)
