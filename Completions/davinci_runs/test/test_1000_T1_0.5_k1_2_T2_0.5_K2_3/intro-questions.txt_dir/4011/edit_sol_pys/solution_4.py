
import sys

def main():
    n = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().strip().split()))
    f = list(map(int, sys.stdin.readline().strip()))
    res = []
    for i in num:
        res.append(f[i-1])
    print(' '.join(map(str, res)))


if __name__ == '__main__':
    main()
