

a, b, c = [int(i) for i in input().split()]

ans = a * b * c

num = [0] * 10

while ans > 0:
    num[ans % 10] += 1
    ans //= 10

for i in num:
    print(i)
