n = int(input())
w = list(map(int, input().split()))


ans = float('inf')


for i in range(n):
    w1 = w[:i]
    w2 = w[i:]
    ans = min(ans, abs(sum(w1) - sum(w2)))

print(ans)
