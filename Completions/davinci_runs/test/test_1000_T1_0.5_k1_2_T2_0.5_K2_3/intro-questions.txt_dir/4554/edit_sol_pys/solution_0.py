
import sys

def main():
    a, b, c = map(int, sys.stdin.readline().split())
    print(max(0, c - (a - b)))

if __name__ == "__main__":
    main()
