

import sys

def main():
    a, b, c, d = map(int, sys.stdin.readline().split())
    p, m, g = map(int, sys.stdin.readline().split())
    aggressiveA = a
    aggressiveC = c
    for i in [P, M, G]:
        if i <= aggressiveA:
            print("both")
        elif i <= aggressiveA + B:
            print("one")
        elif i <= aggressiveA + B + aggressiveC:
            print("both")
        elif i <= aggressiveA + B + aggressiveC + D:
            print("one")
        else:
            print("none")

main()
