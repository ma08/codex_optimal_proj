
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

g = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = [int(x) for x in input().split()]
    g[a-1].append(b-1)
    g[b-1].append(a-1)

visited = [False] * n

def dfs(x):
    visited[x] = True
    for next in g[x]:
        if visited[next]:
            continue
        dfs(next)

dfs(0)

if all(visited):
    print("YES")
else:
    print("NO")

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b, c = [int(x) for x in input().split()]

g = gcd(gcd(a, b), c)

print(min(a//g, b//g, c//g)*7)
