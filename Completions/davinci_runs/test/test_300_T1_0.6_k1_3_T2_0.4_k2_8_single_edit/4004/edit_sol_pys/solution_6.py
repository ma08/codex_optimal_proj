
def solve(n, a):
    d = a[0]
    for i in range(1, n):
        d = gcd(d, a[i])
    return d


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a % b)

n = int(input())
a = [int(x) for x in input().split()]

print(solve(n, a))
