
import sys

def main():
    n, k = map(int, sys.stdin.readline().rstrip().split())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    a.sort()
    print(a)

if __name__ == '__main__':
    main()
