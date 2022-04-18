

import sys

def main():
    n = int(sys.stdin.readline())
    m = 1
    while m < n:
        m *= 3
    print(m)

if __name__ == "__main__":
    main()
