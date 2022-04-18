def gcd(a, b): return a if b == 0 else gcd(b, a % b)

n = int(input())
a = list(map(int, input().split()))

x = a[0]
for i in range(1, n):
    x = gcd(x, a[i])

a = [i // x for i in a]
a.sort()

y = a[0]
for i in range(n):
    if a[i] % y != 0:
        y = gcd(y, a[i])

if y == 1:
    print(-1)
else:
    print(x * y)
