
N, K = map(int, input().split())
temps = list(map(int, input().split(' ')))

ans = 0
for i in range(N-K+1):
    avg = sum(temps[i:i+K]) / K
    ans = max(ans, avg)

print(ans)
