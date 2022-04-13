
n = int(input())
a = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

g = a[0]
for i in range(1, n):
    g = gcd(g, a[i])

for i in range(n):
    a[i] //= g

print(g)
