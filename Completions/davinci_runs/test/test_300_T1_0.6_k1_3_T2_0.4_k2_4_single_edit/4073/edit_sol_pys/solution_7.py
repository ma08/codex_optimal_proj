
def solve(a, b):
    n = len(a)
    c = [0]
    for i in range(n):
        c.append(c[i] + a[i])
        c.append(c[i] - a[i])
    c.sort()
    d = [0]
    for i in range(1, len(c)):
        if c[i] != c[i-1]:
            d.append(c[i])
    m = len(d)
    # dp[i][j] = whether it's possible to have j people
    # and use people from the first i groups
    dp = [[False for j in range(m)] for i in range(n)]
    for i in range(n):
        dp[i][0] = True
    for i in range(n):
        for j in range(1, m):
            dp[i][j] = dp[i][j-1] or (dp[i-1][j-1] and d[j] == d[j-1] + a[i])
    for j in range(m):
        if dp[n-1][j]:
            return j + 1
    return 0
n, m = map(int, raw_input().split())
a = map(int, raw_input().split())
b = map(int, raw_input().split())
c = solve(a, b)
d = solve(b, a)
if c == 0 or d == 0:
    print "No"
else:
    print "Yes"
