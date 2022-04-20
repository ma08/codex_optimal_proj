import sys
sys.setrecursionlimit(10**7)

def dfs(v, p):
    if v == 0:
        return 0
    elif v == 1:
        return 1
    elif v == 2:
        return 2
    elif v == 3:
        return 3

    if p[v] != -1:
        return p[v]

    p[v] = dfs(v-1, p) + dfs(v-2, p) + dfs(v-3, p)
    return p[v]

def main():
    n = int(input())
    p = [-1] * (n+1)
    print(dfs(n, p))

main()

"""


n = int(input())

ans = 0
for i in range(1, n+1):
    num = len(str(i))
    if num % 2 != 0:
        ans += 1

"""
print(ans)
