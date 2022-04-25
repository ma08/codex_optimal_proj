
import sys
sys.setrecursionlimit(1 << 25)
read = sys.stdin.readline
ra = range
enu = enumerate


def main():
    N, M = map(int, read().split())
    AB = [list(map(int, read().split())) for _ in ra(M)]
    CD = [list(map(int, read().split())) for _ in ra(M)]

    G = [[] for _ in ra(N)]
    for a, b in AB:
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    for c, d in CD:
        G[c - 1].append(d - 1)
        G[d - 1].append(c - 1)

    def dfs(v, pre, cnt):
        cnt += 1
        for to in G[v]:
            if to == pre:
                continue
            cnt = dfs(to, v, cnt)
        return cnt

    print(M - dfs(0, -1, 0))


if __name__ == '__main__':
    main()
