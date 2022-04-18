
import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    for i in range(n):
        S = sys.stdin.readline().rstrip()
        if len(S) == 1:
            print(int(S))
        elif len(S) == 2:
            print(int(S) + int(S[0]))
        elif len(S) == 3:
            print(int(S) + int(S[0]) + int(S[1]))
        else:
            print(int(S) + int(S[0]) + int(S[1]) + formula_evaluation(S[2:]))

if __name__ == '__main__':
    main()
