

import sys

def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]
    l.sort()
    print(solve(l, A, B, C, N))

def solve(l, A, B, C):
    if l[0] >= A and l[1] >= B and l[2] >= C:
        return 0
    elif (l[0] + l[1] + l[2] >= A + B + C) and (l[0] + l[1] >= A + B or l[1] + l[2] >= B + C or l[0] + l[2] >= A + C):
        return 10
    else:
        return 10 + solve(l[1:], A - l[0], B - l[0], C - l[0])

if __name__ == '__main__':
    main()
