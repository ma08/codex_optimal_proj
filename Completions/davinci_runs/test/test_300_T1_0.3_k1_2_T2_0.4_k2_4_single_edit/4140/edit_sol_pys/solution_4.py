
import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    a.sort()
    print(a[0], a[-1])

if __name__ == '__main__':
    main()
