import numpy as np

def solve(A,B,C,I,J,K):
    A -= I
    B -= J
    C -= K
    if A <= 0 and B <= 0 and C <= 0:
        return True
    A += I
    B += J
    C += K
    if I == J:
        if I == K:
            if A == B and B == C:
                return True
            else:
                return False
        else:
            if A == B:
                return True
            else:
                return False
    elif I == K:
        if A == C:
            return True
        else:
            return False
    elif J == K:
        if B == C:
            return True
        else:
            return False
    else:
        return False



def main():
    A,B,C = map(int,input().split(' '))
    I,J,K = map(int,input().split(' '))
    if solve(A,B,C,I,J,K):
        print("Yes")
    else:
        print("No")

main()
