
import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    c = []
    for i in range(n):
        c.append((a[i] + b[i]) % n)
    c.sort()
    for i in range(n):
        print(c[i], end = ' ')

if __name__ == '__main__':
    main()
