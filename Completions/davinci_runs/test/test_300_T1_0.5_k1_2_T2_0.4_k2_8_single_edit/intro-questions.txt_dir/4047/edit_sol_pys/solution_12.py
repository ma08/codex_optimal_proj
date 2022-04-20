
import sys

def main():
    n = int(sys.stdin.readline())
    x = list(map(int, sys.stdin.readline().split()))
    x.sort()
    if n % 2 == 0:
        print(x[n//2] - x[n//2 - 1])
    else:
        print(0)

if __name__ == "__main__":
    main()
