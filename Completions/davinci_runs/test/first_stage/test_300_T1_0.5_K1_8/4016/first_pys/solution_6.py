

import sys

def main():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    t = input().strip()
    s = t
    for _ in range(k-1):
        s += t[1:]
    print(s)

if __name__ == "__main__":
    main()