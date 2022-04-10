

# Solution 

#!/usr/bin/python

n, m, d = map(int, raw_input().split())
c = map(int, raw_input().split())

if sum(c) > n:
    print "NO"
    exit()

if d == 1:
    print "YES"
    print " ".join(map(str, [0] * (n + 2)))
    exit()

def solve(n, m, d, c):
    p = [0] * (n + 2)
    p[0] = -1
    p[n + 1] = -1
    pos = 1
    for i in range(m):
        for j in range(c[i]):
            p[pos] = i + 1
            pos += 1
    for i in range(n + 2):
        if p[i] == 0:
            p[i] = -1
    return p

p = solve(n, m, d, c)

ans = []
for i in range(n + 2):
    ans.append(p[i])

for i in range(n + 2):
    if p[i] > 0:
        if p[i - 1] == 0 and i - 1 >= 0:
            ans[i - 1] = p[i]
        elif p[i + 1] == 0 and i + 1 <= n + 1:
            ans[i + 1] = p[i]

if -1 in ans:
    print "NO"
else:
    print "YES"
    print " ".join(map(str, ans))