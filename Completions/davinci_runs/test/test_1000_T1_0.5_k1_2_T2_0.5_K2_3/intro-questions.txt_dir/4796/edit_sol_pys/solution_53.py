
import sys

def get_input():
    A, B, C = map(int, sys.stdin.readline().split())  # A, B, C are the amount of ingredients
    I, J, K = map(int, sys.stdin.readline().split())  # I, J, K are the amount of ingredients needed for one coctail
    return A, B, C, I, J, K

def get_leftovers(A, B, C, I, J, K):
    max_coctails = min(A/I, B/J, C/K)  # maximum number of coctails you can make
    return A - max_coctails*I, B - max_coctails*J, C - max_coctails*K  # return the leftovers

def main():
    A, B, C, I, J, K = get_input()
    A, B, C = get_leftovers(A, B, C, I, J, K)
    print("%.6f %.6f %.6f" % (A, B, C))

if __name__ == "__main__":
    main()
