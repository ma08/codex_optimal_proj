

import sys

def main():
    m, n = map(int, sys.stdin.readline().split())
    if m < 8:
        print("unsatisfactory")
    else:
        print("satisfactory")

if __name__ == "__main__":
    main()
