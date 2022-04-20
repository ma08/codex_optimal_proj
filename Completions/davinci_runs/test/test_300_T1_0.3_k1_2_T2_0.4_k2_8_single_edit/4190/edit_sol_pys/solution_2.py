
import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    c = [((a[i] + b[i]) % n) for i in range(n)]
    print(*sorted(c))

if __name__ == '__main__':
    main()
