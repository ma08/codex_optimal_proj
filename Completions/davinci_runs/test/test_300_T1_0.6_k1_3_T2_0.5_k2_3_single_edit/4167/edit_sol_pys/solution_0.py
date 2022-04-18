import sys

def get_triples(n, k):
    ans = 0
    for a in range(1, n+1):
        for b in range(a, n+1):
            c = a + b
            if c % k == 0 and c <= n:
                ans += 1
    return ans

n, k = map(int, sys.stdin.readline().split())
print(get_triples(n, k))
