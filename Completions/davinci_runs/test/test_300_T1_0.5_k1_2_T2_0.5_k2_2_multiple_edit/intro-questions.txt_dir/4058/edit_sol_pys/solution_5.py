import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    print(a)

if __name__ == '__main__':
    main()
