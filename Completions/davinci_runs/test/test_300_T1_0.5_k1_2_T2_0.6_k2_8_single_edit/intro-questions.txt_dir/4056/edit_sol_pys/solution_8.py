
n = int(input())
a = list(map(int, input().split()))


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

ans = a[0]
for i in range(1, n):
    ans = lcm(ans, a[i])

print(ans)
