
import math
import sys

def main():
    N, K = list(map(int, sys.stdin.readline().split()))
    a = list(map(int, sys.stdin.readline().split()))[:N]
    a.sort(reverse=True)
    print(a)
    print(math.ceil(N / K))


if __name__ == '__main__':
    main()
