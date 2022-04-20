
import sys
import math
N = int(input())

moves = 0

for i in range(1,N+1):
    if(i*i >= N):
        moves = i
        break

print(2*moves-2)
