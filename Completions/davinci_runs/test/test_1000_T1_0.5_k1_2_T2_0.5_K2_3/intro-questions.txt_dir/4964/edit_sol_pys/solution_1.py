
from collections import defaultdict
from heapq import heapify, heappush, heappop
# Solution
def solve():
    N, H, L = map(int, input().split())
    horror_list = set(map(int, input().split()))
    similarities = [list(map(int, input().split())) for _ in range(L)]
    HI = [float('inf')] * N
    adj_list = defaultdict(list)
    for a, b in similarities:
        adj_list[a].append(b)
        adj_list[b].append(a)

            HI[i] = float('inf')
    for a, b in similarities:
        if HI[a] < HI[b]:
            HI[b] = HI[a] + 1
        elif HI[b] < HI[a]:
            HI[a] = HI[b] + 1
    print(HI.index(max(HI)))

solve()
