
import sys

def solve(s, m, p):
    n = len(s)
    res = [0] * 26
    for i in range(n):
        res[ord(s[i]) - ord('a')] += 1
    for i in range(m):
        res[ord(s[p[i] % n]) - ord('a')] += 1
    return res

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        s = sys.stdin.readline()
        p = list(map(int, sys.stdin.readline().split()))
        res = solve(s, m, p)
        print(' '.join(map(str, res)))

if __name__ == '__main__':
    main()
