import math


N, K = map(int, input().split())

ans = 0
for i in range(1, N+1):
    point = 1 / N
    point *= (1 / 2) ** math.ceil(math.log2(K / i))
    ans += point

print(odd_count / N)
