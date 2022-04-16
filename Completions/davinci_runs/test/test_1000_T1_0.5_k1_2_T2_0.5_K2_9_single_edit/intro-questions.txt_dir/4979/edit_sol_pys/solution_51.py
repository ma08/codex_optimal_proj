import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(int(bin(n)[:1:-1], 2))
