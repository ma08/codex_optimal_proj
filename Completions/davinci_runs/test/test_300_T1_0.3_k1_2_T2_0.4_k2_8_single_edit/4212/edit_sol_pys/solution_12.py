
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    for i in range(n):
        for j in range(m):
            print(a[i] * b[j], end=' ')
        print()

if __name__ == '__main__':
    main()
