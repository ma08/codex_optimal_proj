

# SOLUTION

n, k, x = map(int, input().split())
a = list(map(int, input().split()))

if x < k:
    print(-1)
    exit(0)

result = sum(a[:k])

for i in range(k, n):
    result += a[i] - a[i - k]

print(result)
