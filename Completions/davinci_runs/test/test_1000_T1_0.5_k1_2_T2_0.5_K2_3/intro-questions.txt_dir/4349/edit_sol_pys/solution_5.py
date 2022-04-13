
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

g = gcd(a[0], b[0])
for i in range(1, n):
    g = gcd(g, a[i])
    g = gcd(g, b[i])

for i in range(n):
    a[i] //= g
    b[i] //= g

c = a[0]
for i in range(1, n):
    c = max(c, a[i])

for i in range(n):
    print(b[i] * c // a[i], end=' ')
