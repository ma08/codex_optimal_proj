

import sys

def main():
    n = int(sys.stdin.readline())
    temperatures = sorted(list(map(int, sys.stdin.readline().split())))
    print(" ".join(map(str, temperatures)))

if __name__ == "__main__":
    main()
