def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

n = int(input())  # 1行目
t = list(map(int, input().split()))  # 2行目

gcd_num = t[0]
for i in range(1, n):
    gcd_num = gcd(gcd_num, t[i])

print(gcd_num)
