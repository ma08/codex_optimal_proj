

n = int(input())
x = list(map(int, input().split()))

ans = 10**9
for i in range(min(x), max(x) + 1):
    ans = min(ans, sum(abs(i - j) for j in x))

print(ans)