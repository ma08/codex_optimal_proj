import sys
import math

n = int(sys.stdin.readline())

for i in range(n):
    a, b = [int(i) for i in sys.stdin.readline().split()]
    print(math.ceil((a+b)/2))
