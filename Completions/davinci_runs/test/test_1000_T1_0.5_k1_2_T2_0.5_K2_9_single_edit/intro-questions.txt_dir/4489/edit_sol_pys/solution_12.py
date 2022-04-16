
import collections
# My Answer
n = int(input())
s = [input() for i in range(n)]
m = int(input())
t = [input() for j in range(m)]

s_count = collections.Counter(s)
t_count = collections.Counter(t)
ans = sum((s_count - t_count).values())
print(ans)

# Others Answer
n = int(input())
s = [input() for i in range(n)]
m = int(input())
t = [input() for i in range(m)]

ans = 0
for i in set(s):
    ans += s.count(i) - t.count(i)
print(ans)
