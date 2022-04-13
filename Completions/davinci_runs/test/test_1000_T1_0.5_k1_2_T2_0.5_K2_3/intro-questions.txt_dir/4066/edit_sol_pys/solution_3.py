

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)

def lcm(a, b):
    return (a*b)//gcd(a, b)

n = int(input())
a = [int(i) for i in input().split()]

max_lcm = lcm(a[0], a[1])
max_i = 1
max_j = 2

for i in range(n):
    for j in range(i+1, n):
        if lcm(a[i], a[j]) > max_lcm:
            max_lcm = lcm(a[i], a[j])
            max_i = i + 1
            max_j = j + 1

print(max_i, max_j)
