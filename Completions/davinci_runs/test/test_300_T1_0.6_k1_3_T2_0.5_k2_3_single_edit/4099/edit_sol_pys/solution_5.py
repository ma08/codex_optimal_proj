

# S = sum(Ai)
# x = M * N - S (0 <= x <= K)
# x = min(x)

N, K, M = map(int, input().split())
A = list(map(int, input().split()))

S = sum(A)
x = M * N - S  # 0 <= x <= K

if x <= 0:
    print(-1)
elif x > K and x < 0:
    print(-1)
else:
    print(x)
