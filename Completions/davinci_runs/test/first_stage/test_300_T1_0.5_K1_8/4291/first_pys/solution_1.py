

import sys

def main():
    n, q = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().rstrip()
    for _ in range(q):
        l, r = map(int, sys.stdin.readline().split())
        print(s[l-1:r].count("AC"))

if __name__ == '__main__':
    main()