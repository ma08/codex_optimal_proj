

def solve(n, a):
    d = a[0] % MOD
    for i in range(1, n):
        d = gcd(d, a[i] % MOD)
    return d


def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(a % b, b)


n = int(input())
a = [int(x) for x in input().split()]

print(solve(n, a))
