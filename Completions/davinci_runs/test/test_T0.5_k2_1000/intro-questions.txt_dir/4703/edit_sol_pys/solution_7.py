import sys

def formula_evaluation(S):
    if len(S) <= 3:
        return sum([int(s) for s in S])
    return sum([int(s) for s in S[:3]]) + formula_evaluation(S[3:])

def main():
    S = sys.stdin.readline().rstrip()
    print(formula_evaluation(S))

if __name__ == '__main__':
    main()
