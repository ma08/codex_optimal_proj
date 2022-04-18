
import math
N = int(input()) 
for _ in range(N):
    x,y = map(int,input().split())
    if x < y:
        print("NO BRAINS")
    else:
        print("MMM BRAINS")
