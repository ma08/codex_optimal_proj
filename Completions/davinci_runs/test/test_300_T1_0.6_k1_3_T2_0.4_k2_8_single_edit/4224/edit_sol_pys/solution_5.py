import sys
sys.setrecursionlimit(10**6)


N, M = map(int, input().split())


def dfs(i, depth, l):
    if depth == M:
        print(*l)
        return
    for j in range(i, N):
        dfs(j, depth+1, l+[j+1])


def main(): 
    dfs(0, 0, [])

if __name__ == '__main__':
    main()
