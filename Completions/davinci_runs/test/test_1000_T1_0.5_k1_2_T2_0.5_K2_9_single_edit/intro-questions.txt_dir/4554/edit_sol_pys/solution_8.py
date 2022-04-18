

import sys

def main():
    w, a, b = map(int, sys.stdin.readline().split())
    print(max(0, a + w - b))

if __name__ == "__main__":
    main()
