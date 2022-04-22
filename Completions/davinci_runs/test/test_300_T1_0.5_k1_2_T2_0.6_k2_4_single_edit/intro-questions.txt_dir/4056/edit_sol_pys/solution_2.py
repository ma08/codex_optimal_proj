

n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = a[0]

def lcm(a, b):
    return a * b // gcd(a, b)

n = int(input())
a = list(map(int, input().split()))

ans = a[0]
for i in range(1, n):
    ans = lcm(ans, a[i])

print(ans)
