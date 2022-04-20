

#-----Solution-----

n = int(input())
x = list(map(int, input().split()))
x.sort()

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

dist = [x[i + 1] - x[i] for i in range(n - 1)]

d = dist[0]
for i in range(1, n - 1):
    d = gcd(d, dist[i])

if d == 1:
    print(1)
    print(x[0])
else:
    count = 0
    for i in range(n):
        if x[i] % d == 0:
            count += 1
    print(count)
    for i in range(n):
        if x[i] % d == 0:
            print(x[i], end = ' ')