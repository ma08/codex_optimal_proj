import sys
import math
# N is the number of files

N = int(input())
# moves is the minimum number of moves to arrange the files

moves = 0

for i in range(1, N+1):
    if(i*i >= N):  # i is the number of rows and columns
        moves = i
        break

print(2*moves-2)
