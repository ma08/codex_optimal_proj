

import sys

def main():
    """
    Input:
        N M
        X_1 X_2 ... X_M
    Output:
        The minimum number of moves required to achieve the objective.
    """
    N, M = map(int, sys.stdin.readline().rstrip().split())
    X = list(map(int, sys.stdin.readline().rstrip().split()))
    X.sort()
    ans = 0
    for i in range(M):
        ans += abs(X[i] - (X[0] + i))
    print(ans)

if __name__ == '__main__':
    main()