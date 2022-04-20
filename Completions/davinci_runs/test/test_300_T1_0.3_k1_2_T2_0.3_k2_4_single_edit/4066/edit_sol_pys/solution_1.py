
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

n = int(input())
a = list(map(int, input().split()))

ans = (1, 2)
for i in range(n):
    for j in range(i + 1, n):
        if lcm(a[i], a[j]) < lcm(a[ans[0]], a[ans[1]]):
            ans = (i, j)
print(ans[0] + 1, ans[1] + 1)
