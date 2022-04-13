
import sys
import math


def main():
    n = int(sys.stdin.readline())
    print(int(n*(n-1)*(n-2)*(n-3)/24))

main()
