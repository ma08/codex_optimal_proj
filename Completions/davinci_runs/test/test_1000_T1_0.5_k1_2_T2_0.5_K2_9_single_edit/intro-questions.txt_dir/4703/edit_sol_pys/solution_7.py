
import sys

def formula_evaluation(S):
    if len(S) <= 1:
        return int(S)
    return int(S[0]) + formula_evaluation(S[1:])

def main():
    S = sys.stdin.readline().rstrip()
    print(formula_evaluation(S))

if __name__ == '__main__':
    main()
