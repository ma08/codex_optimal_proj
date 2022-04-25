
import sys

def main():
    n = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().strip().split()))
    f = list(map(int, sys.stdin.readline().strip().split()))
    for i in range(n):
        print(f[num[i]-1], end=' ')


if __name__ == '__main__':
    main()
