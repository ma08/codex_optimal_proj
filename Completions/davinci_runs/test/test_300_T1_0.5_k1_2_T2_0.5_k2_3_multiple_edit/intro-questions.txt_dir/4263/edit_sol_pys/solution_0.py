import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    b = list(map(int, sys.stdin.readline().split()))
    b.sort()
    c = list(map(int, sys.stdin.readline().split()))
    c.sort()
    d = list(map(int, sys.stdin.readline().split()))
    d.sort()


if __name__ == '__main__':
    main()
