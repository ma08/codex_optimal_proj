

import sys

def main():
    N, A, B, C = map(int, sys.stdin.readline().split())
    l = [int(sys.stdin.readline()) for _ in range(N)]
    l.sort()
    print(solve(l, A, B, C))

def solve(l, A, B, C):
    if l[0] >= A and l[1] >= B and l[2] >= C:
        return 0
    elif (l[0] + l[1] + l[2] >= A + B + C) and (l[0] + l[1] >= A + B or l[1] + l[2] >= B + C or l[0] + l[2] >= A + C):
        return 10
    else:
        return 10 + solve(l[3:], A - l[0], B - l[1], C - l[2])

if __name__ == '__main__':
    main()
