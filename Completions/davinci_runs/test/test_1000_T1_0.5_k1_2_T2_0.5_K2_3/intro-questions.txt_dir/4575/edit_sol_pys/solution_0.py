# coding:utf-8
n = int(input())
d, x = map(int, input().split())
a = [int(input()) for i in range(n)]
for i in range(n):
    for j in range(1, d+1):
        if j % (a[i] + 1) == 0:
            x -= 1
print(x)
