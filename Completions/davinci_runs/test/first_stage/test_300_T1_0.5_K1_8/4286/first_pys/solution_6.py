

from sys import stdin

def main():
    n, m = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    d = {}
    for i in range(1, n+1):
        d[i] = []
    for i in range(m):
        x, y, w = map(int, stdin.readline().split())
        d[x].append((y, w))
        d[y].append((x, w))
    q = []
    q.append(1)
    used = [0] * (n+1)
    used[1] = 1
    ans = 0
    while len(q) > 0:
        v = q.pop(0)
        for u, w in d[v]:
            if not used[u]:
                used[u] = 1
                q.append(u)
                ans += w
    for i in range(1, n+1):
        if not used[i]:
            ans += a[i-1]
    print(ans)

if __name__ == '__main__':
    main()