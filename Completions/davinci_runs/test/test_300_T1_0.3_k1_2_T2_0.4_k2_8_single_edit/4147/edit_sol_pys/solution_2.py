
import sys

def main():
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    C = list(map(int, sys.stdin.readline().split()))
    print(solve(N, A, B, C))

def solve(l, A, B, C):
    if l[0] >= A and l[1] >= B and l[2] >= C:
        return 0
    elif (l[0] + l[1] + l[2] >= A + B + C) and (l[0] + l[1] >= A + B or l[1] + l[2] >= B + C or l[0] + l[2] >= A + C):
        return 10
    else:
        return 10 + solve(l[1:], A - l[0], B - l[0], C - l[0])

if __name__ == '__main__':
    main()
