

import sys
import os
import heapq
import math

def main():
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    segs = []
    for i in range(m):
        l, r = [int(x) for x in input().split()]
        segs.append([l, r])
    segs = sorted(segs, key=lambda x: (x[1] - x[0], x[0]))
    #print(segs)
    mn = min(a)
    mx = max(a)
    ans = mx - mn
    print(ans)
    if ans == 0:
        print(0)
        return
    used = [False for _ in range(m)]
    for i in range(m):
        if not used[i] and a[segs[i][0]-1] == mn and a[segs[i][1]-1] == mx:
            used[i] = True
            break
        if not used[i] and a[segs[i][0]-1] == mn:
            for j in range(i+1, m):
                if not used[j] and a[segs[j][1]-1] == mx:
                    used[j] = True
                    break
            used[i] = True
            break
        if not used[i] and a[segs[i][1]-1] == mx:
            for j in range(i+1, m):
                if not used[j] and a[segs[j][0]-1] == mn:
                    used[j] = True
                    break
            used[i] = True
            break
    print(used.count(True))
    for i in range(m):
        if used[i]:
            print(i+1, end=' ')
    print()
    #print(used)
    #print(segs)

if __name__ == "__main__":
    main()