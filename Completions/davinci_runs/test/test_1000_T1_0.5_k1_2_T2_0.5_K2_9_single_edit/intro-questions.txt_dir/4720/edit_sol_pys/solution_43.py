
import sys
sys.setrecursionlimit(10**8)

N, M = map(int, input().split())
A = list(map(int, input().split()))

def mod_comb(n, k, mod=10**9+7):
    """
    nCkをmodで割った余りを求める
    """
    if n < 0 or k < 0 or n < k: return 0
    if n == 0 or k == 0: return 1
    if k > n - k: k = n - k
    c = 1
    for i in range(k):
        c = c * (n - i) % mod
        c = c * pow(i+1, mod-2, mod) % mod
    return c

print(s)
