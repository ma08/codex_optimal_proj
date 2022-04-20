import math
n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

temp = []
for i in range(n):
    temp.append(t - h[i] * 0.006)

temp_diff = []
for i in range(n):
    temp_diff.append(abs(temp[i] - a))

print(temp_diff.index(min(temp_diff)) + 1)
