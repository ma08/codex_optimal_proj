# coding: utf-8

N = int(input())
count = 0
seats = [0 for i in range(100)]
for i in range(N):
    l, r = map(int, input().split())
    for j in range(l-1, r):
        seats[j] += 1
for i in range(len(seats)):
    if seats[i] > 0:
        count += 1
print(count)
