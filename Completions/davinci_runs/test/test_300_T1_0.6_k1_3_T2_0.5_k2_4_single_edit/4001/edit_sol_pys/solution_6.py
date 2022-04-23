def lcm(a, b):
    return a * b // gcd(a, b)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


n = int(input())
divisors = list(map(int, input().split()))

x = 1
y = 1

while divisors:
    d = divisors.pop(0)
    if divisors and divisors[0] == d:
        divisors.pop(0)
        x *= d
    else:
        y *= d

print(x, y)
