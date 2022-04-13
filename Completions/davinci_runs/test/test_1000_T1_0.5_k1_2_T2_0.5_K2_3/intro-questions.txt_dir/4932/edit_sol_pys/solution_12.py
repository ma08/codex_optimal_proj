import sys

def main():
    A, B, C, D = map(int, sys.stdin.readline().split())
    P, M, G = map(int, sys.stdin.readline().split())
    aggressiveA = A  # 상대방이 적게 맞으면 이긴다
    aggressiveC = C  # 상대방이 많이 맞으면 이긴다
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
