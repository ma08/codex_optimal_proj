

n = int(input())
a = [int(i) for i in input().split()]

def gcd(a, b, c):
    if a == 0 and b == 0:
        return c
    elif a == 0:
        return gcd(b%c, a, c)
    else:
        return gcd(b%a, a, c)

def lcm(a, b, c):
    return (a*b)//c

n = int(input())
a = [int(i) for i in input().split()]

min_lcm = lcm(a[0], a[1], gcd(a[0], a[1], max(a[0], a[1])))
min_i = 1
min_j = 2

for i in range(n):
    for j in range(i+1, n):
        if lcm(a[i], a[j], gcd(a[i], a[j], max(a[i], a[j]))) < min_lcm:
            min_lcm = lcm(a[i], a[j], gcd(a[i], a[j], max(a[i], a[j])))
            min_i = i + 1
            min_j = j + 1

print(min_i, min_j)
