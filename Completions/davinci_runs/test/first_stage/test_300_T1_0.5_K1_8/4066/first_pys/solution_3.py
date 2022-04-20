

def lcm(x, y):
    return x * y // gcd(x, y)

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

n = int(input())
a = [int(x) for x in input().split()]

min_lcm = 10**7
for i in range(n):
    for j in range(i + 1, n):
        if lcm(a[i], a[j]) < min_lcm:
            min_lcm = lcm(a[i], a[j])
            ans = (i + 1, j + 1)

print(ans[0], ans[1])