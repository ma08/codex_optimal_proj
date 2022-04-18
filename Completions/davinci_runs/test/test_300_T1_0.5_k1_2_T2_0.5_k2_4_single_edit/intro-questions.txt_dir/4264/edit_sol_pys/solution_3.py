

import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = list(map(int, rl().split()))
    
    ans = []
    for ai in A:
        ans.append(ai)
        while len(ans) >= 2 and ans[-1] == ans[-2]:
            ans.pop()
            ans.pop()
    print(len(ans))


if __name__ == '__main__':
    solve()

N = int(input())

count = 0
for i in range(1, N+1):
    count += len(str(i)) % 2

print(count)
