import sys
import math



def main():
    N = int(input())
    A = list(map(int, input().split()))[:N]
    A.sort()
    print(A[0])
    print(A[-1])


if __name__ == '__main__':
    main()
