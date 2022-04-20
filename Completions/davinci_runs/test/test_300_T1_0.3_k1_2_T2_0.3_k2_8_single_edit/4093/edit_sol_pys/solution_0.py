
import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        if n == 1:
            print(0)
        elif m == 0 or m == n:
            print(n-1)
        else:
            print(m)

if __name__ == "__main__":
    main()
