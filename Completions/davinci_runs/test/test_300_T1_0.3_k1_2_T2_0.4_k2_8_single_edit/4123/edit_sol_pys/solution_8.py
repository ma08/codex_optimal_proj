from collections import Counter
n = int(input())
s = input()
c = Counter(s)
ans = 0
for i in c:
    ans += c[i] * (c[i] - 1) // 2


print(ans)
