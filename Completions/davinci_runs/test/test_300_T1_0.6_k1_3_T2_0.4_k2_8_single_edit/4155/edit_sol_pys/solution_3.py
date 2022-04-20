import sys
sys.setrecursionlimit(10**6)


def dfs(G, v, seen):
    seen[v] = True
    for next_v in G[v]:
        if seen[next_v]:
            continue
        dfs(G, next_v, seen)

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for i in range(N):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    seen = [False] * N
    count = 0
    for i in range(N):
        if seen[i]:
            continue
        dfs(G, i, seen)
        count += 1

    print(count)
if __name__ == '__main__':
    main()
