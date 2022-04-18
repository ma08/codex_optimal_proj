

import math
from collections import deque
from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)

def main():
    n = int(input())
    v = list(map(int, input().split()))

    a = [0] * (10**5 + 1)
    for i in v:
        a[i] += 1

    a.sort()

    ans = 0
    if a[-1] == a[-2]:
        ans = 0
    else:
        ans = a[-1] - a[-2]

    print(ans)

if __name__ == '__main__':
    main()
