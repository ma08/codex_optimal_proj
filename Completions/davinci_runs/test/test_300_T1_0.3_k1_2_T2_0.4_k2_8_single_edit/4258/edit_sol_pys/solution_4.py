
n, k = map(int, input().split())
print(k * (n // k) + min(n % k, k // 2))
