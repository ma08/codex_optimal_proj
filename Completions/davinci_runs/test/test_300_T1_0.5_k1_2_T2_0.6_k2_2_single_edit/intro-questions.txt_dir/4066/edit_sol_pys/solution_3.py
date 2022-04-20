import math


n = int(input())
a = [int(i) for i in input().split()]

def gcd(x, y):
    if x == 0:
        return y
    return gcd(y%x, x)

def lcm(a, b):
    return (a*b)//gcd(a, b)

min_lcm = lcm(a[0], a[1])
min_i = 1
min_j = 2
for i in range(n):
    for j in range(i+1, n):
        if lcm(a[i], a[j]) <= min_lcm:
            min_lcm = math.gcd(a[i], a[j])
            min_i = i + 1
            min_j = j + 1
print(min_i, min_j)
