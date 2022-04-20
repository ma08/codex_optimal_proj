
import sys

def main():
    n = int(sys.stdin.readline())  # type: int
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    c = []  # type: list
    for i in range(n):
        c.append((a[i] + b[i]) % n)
    c.sort()
    for i in range(n):
        print(c[i], end=' ')

if __name__ == '__main__':
    main()
