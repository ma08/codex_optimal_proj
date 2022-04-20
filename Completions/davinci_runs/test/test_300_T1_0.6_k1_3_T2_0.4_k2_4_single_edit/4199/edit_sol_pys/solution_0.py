
import sys
import math

N = int(sys.stdin.readline())

result = 0.0

for i in range(N):
    x, u = map(str, sys.stdin.readline().split())
    x = float(x)
    if u == "JPY":
        result += x
    else:
        result += x * 380000.0

print(result) 
