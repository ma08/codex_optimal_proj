
import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    g = a[0]
    for i in range(1, n):
        g = gcd(g, a[i])
    print(g)

if __name__ == '__main__':
    main()
