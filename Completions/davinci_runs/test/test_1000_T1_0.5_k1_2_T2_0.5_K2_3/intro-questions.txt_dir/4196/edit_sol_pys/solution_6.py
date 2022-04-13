import math

def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)

n = int(input())
a_list = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        ans = max(ans, gcd(a_list[i], a_list[j]))

print(ans)
