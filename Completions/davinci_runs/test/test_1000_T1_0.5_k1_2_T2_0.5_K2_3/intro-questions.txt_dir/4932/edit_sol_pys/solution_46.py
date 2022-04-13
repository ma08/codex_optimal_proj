import sys

def main():
    A, B, C, D = map(int, sys.stdin.readline().split())
    P, M, G = map(int, sys.stdin.readline().split())
    aggressiveA = A # 상대방이 적게 맞으면 진다
    aggressiveC = C # 상대방이 많이 맞으면 진다
    for i in [P, M, G]:
        if i <= A:
            print("both")
        elif i <= A + B:
            print("one")
        elif i <= A + B + C:
            print("both")
        elif i <= A + B + C + D:
            print("one")
        else:
            print("none")

main()
