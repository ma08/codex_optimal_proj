import math

N, W, H = map(int, input().split())

for i in range(N):
    match = int(input())
    if match <= W or match <= H or match <= math.sqrt(W**2 + H**2):
        print("DA")
    else:
        print("NE")
