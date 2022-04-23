
import sys
from collections import defaultdict

def minCost(s, k):
  cost = 0
  while k > 0:
    counts = defaultdict(int)
    for c in s:
      counts[c] += 1
    maxCount = max(counts.values())
    cost += (len(s) - maxCount)
    s = s[:maxCount]
    k -= 1
  return cost

if __name__ == "__main__":
  k = int(sys.stdin.readline())
  s = sys.stdin.readline().strip().split()
  print(minCost(s, k))
