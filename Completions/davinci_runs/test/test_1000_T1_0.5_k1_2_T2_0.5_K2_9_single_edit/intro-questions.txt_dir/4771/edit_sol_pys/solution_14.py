
import sys

n = int(input())
v = int(input())

max_v = 0

for i in range(n):
    l, w, h = [int(j) for j in input().split()]
    max_v = max(max_v, l*w*h)

print(max_v-v)
