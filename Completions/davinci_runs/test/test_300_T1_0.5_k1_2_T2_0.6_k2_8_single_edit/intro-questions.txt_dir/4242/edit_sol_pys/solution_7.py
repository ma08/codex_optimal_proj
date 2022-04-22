
def gcd(x, y):
    x, y = abs(x), abs(y)
    while y:
        x, y = y, x % y
    return x

a, b, k = map(int, input().split())

g = gcd(a, b)

divisors = []
for i in range(1, int(g ** 0.5) + 1):
    if g % i == 0:
        divisors.append(i)
        if i != g // i:
            divisors.append(g // i)

divisors.sort(reverse=True)

print(divisors[k - 1])
