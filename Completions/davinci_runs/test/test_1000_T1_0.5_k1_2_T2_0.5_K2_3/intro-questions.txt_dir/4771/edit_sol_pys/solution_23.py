import sys
import math

n = int(input())
V = int(input())

max_volume = 0

for i in range(n):
    l, w, h = [int(j) for j in input().split()]   #list comprehension
    max_volume = max(max_volume, l*w*h)           #max function

print(max_volume-V)
