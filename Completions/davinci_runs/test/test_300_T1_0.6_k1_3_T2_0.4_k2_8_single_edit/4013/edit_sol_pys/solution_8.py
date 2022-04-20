#coding:utf-8

n = int(input())
a = list(map(int, input().split()))
a.sort()
if n == 2:
    print(0)
else:
    print(min(a[n-2]-a[0], a[n-1]-a[1]))
