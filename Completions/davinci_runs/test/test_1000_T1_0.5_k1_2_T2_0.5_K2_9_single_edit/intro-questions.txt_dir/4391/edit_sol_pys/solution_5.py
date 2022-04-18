
n, k = map(int, input().split())
temps = list(map(int, input().split()))

ans = 0
for i in range(n-k+1):
    ans = max(ans, sum(temps[i:i+k]) / k)

print(ans)
