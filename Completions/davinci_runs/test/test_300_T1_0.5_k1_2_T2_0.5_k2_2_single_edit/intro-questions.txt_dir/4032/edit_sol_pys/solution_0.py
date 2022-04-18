import math



def main():
    A, B, C = map(int, input().split())
    if A == B and B == C:
        print(A)
    elif A == B or B == C or C == A:
        print(A + B + C - max(A, B, C))
    else:
        print(A + B + C)

if __name__ == '__main__':
    main()
