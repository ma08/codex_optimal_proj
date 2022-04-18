import sys

N, T = map(int, sys.stdin.readline().rstrip().split())  # N: # of stops, T: time limit
t = list(map(int, sys.stdin.readline().rstrip().split()))  # t[i]: time when the i-th stop is reached

total = 0  # total time
start = 0  # time when the bus starts

for i in range(N):
    if t[i] < start:  # if the bus arrives before the next stop
        total += T
    else:  # if the bus arrives after the next stop
        total += T + t[i] - start
        start = t[i]

print(total)
