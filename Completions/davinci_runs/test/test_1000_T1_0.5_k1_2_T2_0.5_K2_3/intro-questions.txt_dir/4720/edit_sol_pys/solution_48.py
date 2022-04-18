# coding: utf-8

N = int(input())
count = 0
seats = [0 for i in range(100000)]
for i in range(N):
    l, r = map(int, input().split())  # 左端と右端
    for j in range(l, r + 1):
        seats[j-1] += 1  # 座席に人がいる
for i in range(len(seats)):
    if seats[i] > 0:
        count += 1
print(count)
