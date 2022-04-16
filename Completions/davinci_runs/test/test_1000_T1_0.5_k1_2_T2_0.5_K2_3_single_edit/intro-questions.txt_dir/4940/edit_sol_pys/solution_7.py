import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(n):
        if a[i] < b[i]:
            print(-1)
            return
    ans = 0
    while True:
        cnt = 0
        for i in range(n):
            if a[i] == b[i]:
                cnt += 1
        if cnt == n:
            break
        ans += 1
        for i in range(n):
            if a[i] % b[i] != 0:
                a[i] = a[i] % b[i]
            else:
                a[i] = b[i]
    print(ans)


if __name__ == '__main__':
    main()
