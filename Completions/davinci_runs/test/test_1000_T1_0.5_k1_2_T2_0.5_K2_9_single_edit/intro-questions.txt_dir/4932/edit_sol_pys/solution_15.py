

import sys

def main():
    A, B, C, D = map(int, sys.stdin.readline().split())
    P, M, G = map(int, sys.stdin.readline().split())
    aggressiveA = A * 2
    aggressiveC = C * 2
    for i in [P, M, G]:
        if i <= aggressiveA:
            print("both")
        elif i <= aggressiveA + B * 2:
            print("one")
        elif i <= aggressiveA + B * 2 + aggressiveC:
            print("both")
        elif i <= aggressiveA + B * 2 + aggressiveC + D * 2:
            print("one")
        else:
            print("none")

main()
