

n = input()
a = [int(x) for x in input().split()]

b = [a[0]]

g = gcd(gcd(a, b), c)

print(min(a//g, b//g, c//g)*7)
