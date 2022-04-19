import sys
import heapq
import bisect
from collections import deque
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, d=DVSR): return pow(x, d - 2, d)
def DIV(x, y, d=DVSR): return (x * INV(y, d)) % d
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def FLIST(n):
    res = [1]
    for i in range(1, n+1): res.append(res[i-1]*i%DVSR)
    return res



def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    i, j = 0, n-1
    ans = 0
    while i <= j:
        if A[i] > k and A[j] > k:
            break
        elif A[i] <= k and A[j] <= k:
            ans += 2
            i += 1
            j -= 1
        elif A[i] <= k:
            ans += 1
            i += 1
        else:
            ans += 1
            j -= 1
    print(ans)

if __name__ == '__main__':
    main()
