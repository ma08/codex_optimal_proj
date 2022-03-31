n = int(input())
a = list(map(int, input().split()))

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def lcm(x, y):
    return (x * y) // gcd(x, y)

min_lcm = float('inf')
for i in range(n):
    for j in range(i+1, n):
        min_lcm = min(min_lcm, lcm(a[i], a[j]))

for i in range(n):
    for j in range(i+1, n):
        if min_lcm == lcm(a[i], a[j]):
            print(i + 1, j + 1)
            break
