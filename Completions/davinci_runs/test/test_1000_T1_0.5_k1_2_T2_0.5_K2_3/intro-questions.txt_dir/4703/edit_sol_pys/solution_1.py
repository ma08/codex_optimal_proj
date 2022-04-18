
import sys

def formula_evaluation(S):
    if len(S) == 0:
        return 0
    if len(S) == 1: # '1'
        return int(S[0])
    if len(S) == 2: # '12'
        return int(S[0]) + int(S)
    if len(S) == 3: # '123'
        return int(S[0]) + int(S[1]) + int(S)
    return int(S[0]) + int(S[1]) + int(S) + formula_evaluation(S[2:])

def main():
    S = sys.stdin.readline().rstrip()
    print(formula_evaluation(S))

if __name__ == '__main__':
    main()
