

import sys

def main():
    q = int(sys.stdin.readline().strip())
    for _ in range(q):
        s = sys.stdin.readline().strip()
        n = int(sys.stdin.readline().strip())
        b = [int(x) for x in sys.stdin.readline().strip().split()]
        print(solve(s, n, b))

def solve(s, n, b):
    s = list(s)
    for i in range(n):
        if i == 0:
            s[0] = chr(ord('a') + sum(b[:1]))
        else:
            s[i] = chr(ord('a') + sum(b[:i]) - sum(b[:i-1]))
    return ''.join(s)

if __name__ == '__main__':
    main()