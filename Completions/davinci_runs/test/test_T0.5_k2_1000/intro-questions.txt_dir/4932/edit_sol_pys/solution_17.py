
import sys

def main():
    A, B, C, D = map(int, sys.stdin.readline().split())
    P, M, G = map(int, sys.stdin.readline().split())
    aggressive_A = A
    aggressive_C = C
    for i in [P, M, G]:
        if i <= aggressive_A:
            print("both")
        elif i <= aggressive_A + B:
            print("one")
        elif i <= aggressive_A + B + aggressive_C:
            print("both")
        elif i <= aggressive_A + B + aggressive_C + D:
            print("one")
        else:
            print("none")

main()
