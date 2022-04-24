
n = int(input())
a = list(map(int, input().split()))


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


max_gcd = 0

for i in range(n):
    for j in range(n):
        if i != j:
            gcd_tmp = gcd(a[i], a[j])
            if max_gcd < gcd_tmp:
                max_gcd = gcd_tmp

print(max_gcd)
