import sys
import math



def main():
    n = int(sys.stdin.readline())
    lengths = list(map(int, sys.stdin.readline().split()))

    print("Yes" if max(lengths) < sum(lengths) - max(lengths) else "No")

if __name__ == '__main__':
    main()
