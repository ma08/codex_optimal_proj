import sys


N = int(sys.stdin.readline())
W = [int(x) for x in sys.stdin.readline().split(' ')]

max_diff = float('inf')
for t in range(1, N):
    s1 = sum(W[:t]) # sum of first t elements
    s2 = sum(W[t:]) # sum of last N-t elements
    if abs(s1-s2) < max_diff: # if the difference is smaller than current max
        max_diff = abs(s1-s2) # update max

print(max_diff)
