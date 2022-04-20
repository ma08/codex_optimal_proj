
import sys

N = int(input())

moves = 0

for i in range(1, N+1):
    if(i*i >= N):  # Check if square of number is greater than or equal to N
        moves = i  # If yes, then that number is the number of moves
        break

print(2*moves-2)
