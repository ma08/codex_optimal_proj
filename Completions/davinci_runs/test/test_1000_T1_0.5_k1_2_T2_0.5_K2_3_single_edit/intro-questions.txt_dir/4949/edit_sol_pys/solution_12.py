

import sys

input = sys.stdin.readline

N, W, H = map(int, input().rstrip().split())

for _ in range(N):
    match = int(input().rstrip())
    if match <= (W**2 + H**2)**0.5:
        print("DA")
    else:
        print("NE")
