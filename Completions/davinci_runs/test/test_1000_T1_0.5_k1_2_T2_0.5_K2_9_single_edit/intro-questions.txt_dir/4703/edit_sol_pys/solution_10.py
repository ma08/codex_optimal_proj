

import sys

    if len(S) == 0:
        return 0
def formula_evaluation(S):
    if len(S) == 1:
        return int(S[0])
    if len(S) == 2:
        return int(S[0]) + int(S[1])
    if len(S) == 3:
        return int(S[0]) + int(S[1]) + int(S[2])
    return int(S[0]) + int(S[1]) + int(S[2]) + formula_evaluation(S[3:])

def main():
    S = sys.stdin.readline().rstrip()
    print(formula_evaluation(S))

if __name__ == '__main__':
    main()
