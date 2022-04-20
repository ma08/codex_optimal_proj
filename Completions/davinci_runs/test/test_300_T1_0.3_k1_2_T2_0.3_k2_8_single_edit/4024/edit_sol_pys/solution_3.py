import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    if k > n:
        print(-1)
        return
    elif k == n:
        print(0)
        return
    else:
        print(n*(k-1))

if __name__ == "__main__":
    main()
