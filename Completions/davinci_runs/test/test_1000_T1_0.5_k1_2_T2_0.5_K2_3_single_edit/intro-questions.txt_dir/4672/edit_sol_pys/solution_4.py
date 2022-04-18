from collections import Counter
n = int(input())
s = Counter(map(int, input().split()))
m = int(input())
ans = 0
for _ in range(m):
    x, y = map(int, input().split())
    if s[x] > 0:
        s[x] -= 1
        ans += y
print(ans)
