
import sys

def solve(s, m, p):
    # TODO: write your code here
    return []

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
