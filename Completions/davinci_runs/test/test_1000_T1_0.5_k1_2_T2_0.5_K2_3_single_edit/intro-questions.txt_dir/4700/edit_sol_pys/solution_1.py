
import sys

n, m = [int(i) for i in input().split()]

h = [int(i) for i in input().split() if i != n]

a = [[int(i) for i in input().split()] for i in input().split() if i != m]

print(n)
print(m)
print(h)
print(a)
