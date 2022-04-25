import sys
import math
from itertools import combinations
from itertools import permutations

def main():
    S = input()
    N = len(S)

    if N == 2:
        if S[0] == S[1]:
            print(1)
        else:
            print(2)
        exit()

    if N == 3:
        if S[0] == S[1] or S[1] == S[2] or S[2] == S[0]:
            print(2)
        else:
            print(3)
        exit()

    for i in range(N - 3):
        if S[i] == S[i + 1] or S[i] == S[i + 2] or S[i + 1] == S[i + 2]:
            print(2)
            exit()

    print(3)

if __name__ == '__main__':
    main()
