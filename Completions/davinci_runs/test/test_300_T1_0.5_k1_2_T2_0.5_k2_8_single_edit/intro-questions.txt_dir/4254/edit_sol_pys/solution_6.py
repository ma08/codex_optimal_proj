
import sys

def main():
    s, w = map(int, sys.stdin.readline().split())
    print("safe" if s > w else "unsafe")

if __name__ == '__main__':
    main()
