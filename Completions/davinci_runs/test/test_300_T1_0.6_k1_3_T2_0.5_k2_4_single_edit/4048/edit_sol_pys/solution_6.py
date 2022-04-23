
import sys
import math

N = int(input())

moves = 1

for i in range(1,N):
    if(i*i == N):
        moves = i*2-1
        break
    elif(i*i > N):
        moves = i*2-2
        break

print(moves)
