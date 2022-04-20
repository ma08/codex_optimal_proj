

def solve(n, m, a):
    a.sort()
    b = a[::-1]
    ans = 0
    for i in xrange(m):
        ans += a[i]
    for i in xrange(n - m):
        ans += b[i]
    return ans
print solve(input(), input(), map(int, raw_input().split()))
