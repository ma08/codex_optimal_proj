# coding: utf-8


n = int(input())  # 数字を入力
a = list(map(int, input().split()))

b = []
c = []

for i in range(n):
    if i % 2 == 0:
        b.append(a[i])
    else:
        c.append(a[i])

if len(b) > len(c):
    print(sum(b[:-1]))
elif len(c) > len(b):
    print(sum(c[:-1]))
else:
    print(sum(b))
