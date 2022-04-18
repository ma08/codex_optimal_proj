
import sys

n = int(input())
l = [1, 1]
for i in range(n):
    l.append(l[i] + l[i+1])
print(l[n])
