

import sys

def main():
    A, B, C = map(int, sys.stdin.readline().split())
    if A == B and A != C:
        print("Yes")
    elif A == C and A != B:
        print("Yes")
    elif B == C and B != A:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()