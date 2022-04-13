
import sys

def solve(s, n, m, p):
    n = len(s)
    res = [0] * n
    for i in range(n - 1):
        res[i + 1] = res[i] + 1 if s[i] == s[i + 1] else res[i]
    for i in range(m):
        res[p[i] % n] += 1
    return res

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        s = sys.stdin.readline()
        s = s.strip()        
        p = list(map(int, sys.stdin.readline().split()))
        res = solve(s, n, m, p)
        print(' '.join(map(str, res)))

if __name__ == '__main__':
    main()
