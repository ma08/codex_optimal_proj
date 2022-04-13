# comment

from math import *

t = int(input())

for i in range(t):
    h, m = map(int, input().split())
    print(int(1440 - (h * 60 + m)))
