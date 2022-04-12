import sys

def solve(s, m, p):
    n = len(s)
    res = [0] * n
    for i in range(n - 1, -1, -1):
        res[i] = res[i + 1] + (s[i] == '1')
    for i in range(m - 1, -1, -1):
        res[p[i] - 1] = res[p[i]]
    return res[:n - 1]

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        s = sys.stdin.readline().strip()
        p = list(map(int, sys.stdin.readline().split()))
        res = solve(s, m, p)
        print(' '.join(map(str, res)))

if __name__ == '__main__':
    main()
