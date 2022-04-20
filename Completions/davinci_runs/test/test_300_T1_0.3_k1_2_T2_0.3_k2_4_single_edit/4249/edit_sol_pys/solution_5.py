
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    a.reverse()
    for i in range(1, n):
        a[i] = max(0, a[i] - i)
    a.sort()
    a.reverse()
    print(m // a[0] + 1)

if __name__ == '__main__':
    main()
