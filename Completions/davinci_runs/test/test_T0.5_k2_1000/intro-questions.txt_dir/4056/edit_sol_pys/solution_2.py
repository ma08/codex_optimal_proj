
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

n = int(input())
a = list(map(int, input().split()))

ans = a[0]
for i in range(1, n):
    ans = lcm(ans, a[i])

print(ans)
