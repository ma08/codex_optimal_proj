import sys

def main():
    A, B, C, D = map(int, sys.stdin.readline().split())
    P, M, G = map(int, sys.stdin.readline().split())
    aggressiveA = A
    aggressiveC = C
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
