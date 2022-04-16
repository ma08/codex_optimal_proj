
import sys
sys.setrecursionlimit(1000000000)
#------------------------------------------------------------------------------#

n, V = map(int, input().split())
volumes = []
for _ in range(n):
    l, w, h = map(int, input().split())
    volumes.append(l * w * h)

print(max(volumes) - V)
