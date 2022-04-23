import sys

def get_triples(n, k, mod):
    ans = [0] * (mod+1)
    for i in range(1, n+1):
        for j in range(i, n+1):
            s = i + j
            ans[s % k] += 1
    return ans[0]

n, k = map(int, sys.stdin.readline().split())
print(get_triples(n, k))
