

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n = int(input())
a = list(map(int, input().split()))

# find gcd of all numbers
g = a[0]
for i in range(1, n):
    g = gcd(g, a[i])

# count divisors of gcd
count = 0
i = 1
while i * i <= g:
    if g % i == 0:
        if g // i == i:
            count += 1
        else:
            count += 2
    i += 1

print(count)