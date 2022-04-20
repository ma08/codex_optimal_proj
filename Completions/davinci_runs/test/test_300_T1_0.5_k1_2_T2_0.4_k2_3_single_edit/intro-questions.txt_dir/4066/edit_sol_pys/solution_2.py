
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a*b)//gcd(a, b)

n = int(input())
a = [int(i) for i in input().split()]

min_lcm = lcm(a[0], a[1])
min_i = 1
min_j = 2

for i in range(n):
    for j in range(i+1, n):
        if lcm(a[i], a[j]) < min_lcm:
            min_lcm = lcm(a[i], a[j])
            min_i = i + 1
            min_j = j + 1

print(min_i, min_j)
