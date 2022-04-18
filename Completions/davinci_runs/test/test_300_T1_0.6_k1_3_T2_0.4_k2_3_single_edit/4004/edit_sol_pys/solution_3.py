

def solve(n, s):
    d = s[0]
    for i in range(1, n): d = gcd(d, s[i])
    return d if d != 1 else -1


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a % b)


n = int(input())
s = [int(x) for x in input().split()]

print(solve(n, s))
