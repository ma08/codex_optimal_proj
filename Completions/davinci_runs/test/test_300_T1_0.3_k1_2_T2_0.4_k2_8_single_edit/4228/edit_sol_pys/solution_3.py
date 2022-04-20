
import sys

def main():
    n, l = map(int, sys.stdin.readline().rstrip().split())
    print(sum(range(l, l+n-1)))

if __name__ == '__main__':
    main()
