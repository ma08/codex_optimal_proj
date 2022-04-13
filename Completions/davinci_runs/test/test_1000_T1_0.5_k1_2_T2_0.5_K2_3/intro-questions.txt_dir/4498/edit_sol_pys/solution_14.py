
import sys

def main():
    a, b, c, d = map(int, sys.stdin.readline().split())
    print("Yes" if abs(a - b) <= d and abs(b - c) <= d else "No")

if __name__ == "__main__":
    main()
