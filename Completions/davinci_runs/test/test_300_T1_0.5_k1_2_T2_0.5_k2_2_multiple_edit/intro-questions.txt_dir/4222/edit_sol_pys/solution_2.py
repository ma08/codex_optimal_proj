
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    survivor = set([i for i in range(1, n+1)])
    for _ in range(k):
        d = int(sys.stdin.readline())
        survivor -= set(map(int, sys.stdin.readline().split()))
    print(len(survivor))

if __name__ == '__main__':
    main()
