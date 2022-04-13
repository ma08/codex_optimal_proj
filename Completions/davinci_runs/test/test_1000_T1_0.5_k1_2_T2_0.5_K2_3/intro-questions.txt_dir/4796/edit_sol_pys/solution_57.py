

import sys
import math

def get_input():
    A, B, C = map(int, sys.stdin.readline().split())
    I, J, K = map(int, sys.stdin.readline().split())
    return A, B, C, I, J, K

def get_left_overs(A, B, C, I, J, K):
    max_cocktails = min(A//I, B//J, C//K)
    return A - max_cocktails*I, B - max_cocktails*J, C - max_cocktails*K, max_cocktails

def main():
    A, B, C, I, J, K = get_input()
    A, B, C, max_cocktails = get_left_overs(A, B, C, I, J, K)
    print("%.6f %.6f %.6f %.6f" % (A, B, C, max_cocktails))

if __name__ == "__main__":
    main()
