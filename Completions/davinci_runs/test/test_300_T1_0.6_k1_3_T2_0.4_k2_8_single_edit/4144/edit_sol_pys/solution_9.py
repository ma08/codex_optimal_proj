import sys
import math
def main():
    N, M = map(int, sys.stdin.readline().split())
    if N == 1 and M == 1:
        print(1)
    elif N == 1 and M != 1:
        print(M - 2)
    elif N != 1 and M == 1:
        print(N - 2)
    else:
        print((N - 2) * (M - 2))

if __name__ == "__main__":
    main()
