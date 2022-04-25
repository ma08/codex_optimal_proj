import sys
import math
import heapq

sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))


n, m = map(int, input().split())
segments = []
for i in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))
segments.sort(key=lambda x: x[0])
# print(segments)
res = []
for i in range(1, m + 1):
    if i not in [seg[0] for seg in segments] and i not in [seg[1] for seg in segments]:
        res.append(i)

print(len(res))
print(*res)
