import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

import sys

def main():
    a, b, c, d = map(int, input().split())
    print(max(a*c, a*d, b*c, b*d))

if __name__ == '__main__':
    main()
