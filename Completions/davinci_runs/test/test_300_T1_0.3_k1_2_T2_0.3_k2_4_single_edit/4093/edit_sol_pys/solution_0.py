
import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        if n == 1:
            print(0)
        elif m == 0:
            print(n-1)
        else:
            print(m-1)

if __name__ == "__main__":
    main()
