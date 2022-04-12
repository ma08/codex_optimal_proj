
import sys

def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    print((n - 1) * (m - 1) + (m - 1))

if __name__ == "__main__":
    main()
