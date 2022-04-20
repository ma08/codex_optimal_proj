

n, k = map(int, input().split())
ans = 0

for i in range(1, k + 1):
    ans += (n // k) * (n // k) * (n // k)
    ans += 3 * (n // k) * (n // k) * ((n % k) - (i % k) + 1)
    ans += 3 * (n // k) * ((n % k) - (i % k) + 1) * ((n % k) - (i % k) + 1)
    ans += ((n % k) - (i % k) + 1) * ((n % k) - (i % k) + 1) * ((n % k) - (i % k) + 1)

print(ans)