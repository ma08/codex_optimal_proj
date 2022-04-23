from collections import Counter

n = int(input())
s = input()

c = Counter(s)

ans = n - sum(c.values()) // 2

print(ans)
