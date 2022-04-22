

import sys
from collections import defaultdict
import math

def main():
    input = sys.stdin.readline
    n, m = map(int, input().rstrip().split())
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    print(solve(n, m, a, b))

def solve(n, m, a, b):
    d = defaultdict(int)
    d[0] = 1
    s = 0
    for i in a:
        s += i
        d[s] += 1
    s = 0
    ans = 0
    for i in b:
        s += i
        ans += d[s]
    return ans

if __name__ == "__main__":
    main()
