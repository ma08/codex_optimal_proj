import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    parts = set()
    for i in range(m):
        parts.add(sys.stdin.readline().strip())
        if len(parts) == n:
            print(i+1)
            return
    print('paradox avoided', file=sys.stderr)

if __name__ == '__main__':
    main()
