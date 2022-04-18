
import sys
from collections import defaultdict

def minCost(n, k, s):
  cost = 0
  while k > 0:
    counts = defaultdict(int)
    for c in s:
    if k > len(s):
      return -1
    if k == 1:
      return cost + len(s)
      counts[c] += 1
    maxCount = max(counts.values())
    cost += (len(s) - maxCount)
    s = s[:maxCount]
    k -= 1
  return cost

if __name__ == "__main__":
  n, k = map(int, sys.stdin.readline().strip().split())
  s = sys.stdin.readline().strip()
  print(minCost(n, k, s))
