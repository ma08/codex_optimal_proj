

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    parts = set()
    for i in range(m):
        parts.add(sys.stdin.readline())
        if len(parts) == n:
            print(i+1)
            return
    print('paradox avoided')

if __name__ == '__main__':
    main()
