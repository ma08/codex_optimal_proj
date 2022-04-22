import math
def lcm(x, y):
    return (x * y) // math.gcd(x, y)
n = int(input())
a = list(map(int, input().split()))
ans = a[0]
for i in range(1, n):
    ans = lcm(ans, a[i])
print(ans)
