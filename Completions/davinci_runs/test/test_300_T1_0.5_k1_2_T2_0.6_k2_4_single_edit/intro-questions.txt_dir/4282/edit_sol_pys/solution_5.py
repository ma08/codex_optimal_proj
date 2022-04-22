import sys


def main():
    sys.setrecursionlimit(10 ** 7)
    N, M = map(int, sys.stdin.readline().split())
    to = [0] * N
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        a -= 1
        b -= 1
        to[a] ^= b
        to[b] ^= a

    def dfs(v, p):
        if to[v] == p:
            return -1
        if to[v] == 0:
            return v
        return dfs(to[v], v)

    for i in range(N):
        print(dfs(i, -1) + 1)


if __name__ == '__main__':
    main()
