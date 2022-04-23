import sys

def solve(s, t):
    if s == t:
        return 0
    elif len(s) < len(t):
        return len(t) - len(s)
    else:
        return len(s) - len(t)

if __name__ == '__main__':
    s = sys.stdin.readline()
    t = sys.stdin.readline()
    print(solve(s, t))
