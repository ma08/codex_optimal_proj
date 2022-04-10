

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n = input()
a = map(int, raw_input().split())

res = a[0]
for i in xrange(1, n):
    res = gcd(res, a[i])

print res