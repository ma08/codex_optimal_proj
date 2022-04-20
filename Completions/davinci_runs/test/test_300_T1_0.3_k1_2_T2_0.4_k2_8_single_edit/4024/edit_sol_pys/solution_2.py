
import math
import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    print(a)
    # print(math.ceil(n/2))

if __name__ == "__main__":
    main()
