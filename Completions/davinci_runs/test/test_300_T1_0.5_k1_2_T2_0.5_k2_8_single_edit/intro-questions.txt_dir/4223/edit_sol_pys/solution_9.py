from collections import Counter

n = int(input())
s = input()

c = Counter(s)

ans = n - c.most_common()[0][1]

print(ans)
