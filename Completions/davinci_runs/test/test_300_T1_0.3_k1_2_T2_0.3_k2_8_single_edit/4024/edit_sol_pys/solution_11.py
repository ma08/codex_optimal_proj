
import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        s = sys.stdin.readline().strip()
        if k > n:
            print(-1)
            continue
        elif k == n:
            print(0)
            continue
        else:
            print(n*(k-1))

if __name__ == "__main__":
    main()
