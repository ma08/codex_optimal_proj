
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(1 if n < k else n // k + n % k)
