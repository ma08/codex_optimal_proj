import sys

    n, p = map(int, sys.stdin.readline().split())
def main():
    carrots = 0
    for i in range(n):
        sys.stdin.readline().strip()
        carrots += p
    print carrots

if __name__ == '__main__':
    main()
