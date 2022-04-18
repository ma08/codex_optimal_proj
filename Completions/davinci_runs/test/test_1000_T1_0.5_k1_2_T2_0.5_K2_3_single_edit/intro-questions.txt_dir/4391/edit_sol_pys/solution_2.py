
n, k = map(int, input().split())
temps = list(map(int, input().split()))

ans = 0
for i in range(n-k+1):
    avg = sum(temps[i:i+k]) / k
    ans = max(ans, avg)

print(ans)
