
a, b, c = [int(x) for x in input().split()]

g = __gcd(__gcd(a, b), c)

print(min(a//g, b//g, c//g)*7)
