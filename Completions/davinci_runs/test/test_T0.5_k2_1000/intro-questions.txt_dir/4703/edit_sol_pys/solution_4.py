import sys

def formula_evaluation(S):
    if len(S) <= 3:
        return sum(map(int, S))
    return sum(map(int, S)) + formula_evaluation(S[2:])

def main():
    S = sys.stdin.readline().rstrip()
    print(formula_evaluation(S))

if __name__ == '__main__':
    main()
