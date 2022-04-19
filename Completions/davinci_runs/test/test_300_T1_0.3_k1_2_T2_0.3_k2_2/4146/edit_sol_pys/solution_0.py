# coding: utf-8

n = int(input())
v = list(map(int, input().split()))

# 同じ数字が連続している場合はそれを消す
# 連続していない場合は、異なる数字が2つしかないので、どちらかを消す
# ただし、同じ数字が連続している場合は、それを消すのが最適
# そのため、同じ数字が連続している場合は、それを消す
# 連続していない場合は、異なる数字が2つしかないので、どちらかを消す

count = 0
for i in range(n-1):
    if v[i] == v[i+1]:
        count += 1

if count == 0:
    print(2)
else:
    print(1)
