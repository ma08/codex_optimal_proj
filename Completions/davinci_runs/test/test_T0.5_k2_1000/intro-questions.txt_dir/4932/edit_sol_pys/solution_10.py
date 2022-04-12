
import sys

def main():
    A, B, C, D = map(int, sys.stdin.readline().split())
    P, M, G = map(int, sys.stdin.readline().split())
    aggressiveA = A + B
    aggressiveC = C + D
    for i in [P, M, G]:
        if i <= aggressiveA:
            print("both")
        elif i <= aggressiveA:
            print("one")
        elif i <= aggressiveA + aggressiveC:
            print("both")
        elif i <= aggressiveA + aggressiveC:
            print("one")
        else:
            print("none")

main()
