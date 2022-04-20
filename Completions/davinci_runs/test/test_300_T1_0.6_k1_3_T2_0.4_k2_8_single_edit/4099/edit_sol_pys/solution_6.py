

# S = sum(A) + x
# x = M * N - S = M * (N - sum(A))

N, K, M = map(int, input().split())
A = list(map(int, input().split()))

S = sum(A)  # sum(A)
x = M * (N - S)  # M * (N - sum(A))

if x < 0:
    print(-1)
elif x > K:
    print(-1)
else:
    print(x)
