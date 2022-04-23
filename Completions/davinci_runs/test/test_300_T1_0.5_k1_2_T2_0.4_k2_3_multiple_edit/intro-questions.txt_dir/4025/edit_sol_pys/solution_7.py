
import math

a, b, c = map(int, input().split())

a, b, c = [int(x) for x in input().split()]

g = gcd(gcd(a, b), c)

print(min(a//g, b//g, c//g)*g)
