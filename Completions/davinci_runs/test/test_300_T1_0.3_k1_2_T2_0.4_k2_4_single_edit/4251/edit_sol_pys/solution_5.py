
from collections import defaultdict
from heapq import heappush, heappop
import sys
import math
import bisect

# ctci.5_9

# Solution

def solve(n):
    ans = []
    for i in range(n+1):
        if i == 0:
            ans.append(0)
        elif i == 1:
            ans.append(1)
        else:
            ans.append(ans[i-1] + ans[i-2])
    return ans[n]

if __name__ == "__main__":
    n = int(input())
    print(solve(n))
