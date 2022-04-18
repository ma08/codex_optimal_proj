
import sys
import math

def get_input():
    A, B, C = map(int, sys.stdin.readline().split()) #A=100, B=100, C=100
    I, J, K = map(int, sys.stdin.readline().split()) #I=1, J=1, K=1
    return A, B, C, I, J, K

def get_leftovers(A, B, C, I, J, K):
    max_cocktails = min(A/I, B/J, C/K) #max_cocktails=100
    return A - max_cocktails*I, B - max_cocktails*J, C - max_cocktails*K #A=0, B=0, C=0

def main():
    A, B, C, I, J, K = get_input()
    A, B, C = get_leftovers(A, B, C, I, J, K) #A=0, B=0, C=0
    print("%.6f %.6f %.6f" % (A, B, C)) #0.000000 0.000000 0.000000

if __name__ == "__main__":
    main()
