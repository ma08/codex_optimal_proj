

import sys
import math

N = int(input())
if N == 1:
    print(0)
else:
    moves = 0
    for i in range(1,N+1):
        if(i*i >= N):
            moves = i
            break
    print(2*moves-2)
