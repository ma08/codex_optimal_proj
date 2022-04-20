

import sys

N, M = list(map(int, sys.stdin.readline().split())) # N, M를 받아서

if N == M: # N, M이 같으면
    print("Yes")
else: # 같지 않으면
    print("No")
