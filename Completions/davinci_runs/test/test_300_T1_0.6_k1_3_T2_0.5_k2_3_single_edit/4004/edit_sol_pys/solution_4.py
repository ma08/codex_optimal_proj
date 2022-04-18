

def solve(n, a, d):
    d = a[0]
    for i in range(1, n):
        d = gcd(d, a[i], d)
    return d


def gcd(a, b, d):
    if a < b:
        return gcd(b, a, d)
    if a % b == 0:
        return b
    return gcd(b, a % b, d)


n = int(input())
a = [int(x) for x in input().split()]

print(solve(n, a))
