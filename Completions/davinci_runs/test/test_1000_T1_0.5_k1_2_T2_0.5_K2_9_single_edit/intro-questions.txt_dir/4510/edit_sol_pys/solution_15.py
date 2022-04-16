

from collections import Counter

n = int(input())
a = list(map(int, input().split()))

b = Counter(a)
b = b.most_common()

ans = 0
for i, j in b:
    if j <= ans:
        break
    ans += 1

print(ans)
