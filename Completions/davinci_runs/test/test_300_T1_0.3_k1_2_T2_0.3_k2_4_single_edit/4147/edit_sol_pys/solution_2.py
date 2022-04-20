
import sys

def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]
    l.sort()
    print(solve(l, A, B, C, 0))

def solve(l, A, B, C, cnt):
    if len(l) == 0:
        return 10 ** 10
    elif len(l) == 1:
        if A == l[0] or B == l[0] or C == l[0]:
            return cnt
        else:
            return 10 ** 10
    elif len(l) == 2:
        if A == l[0] + l[1] or B == l[0] + l[1] or C == l[0] + l[1]:
            return cnt
        else:
            return 10 ** 10
    else:
        return min(solve(l[1:], A, B, C, cnt), solve(l[1:], A - l[0], B, C, cnt + 10), solve(l[1:], A, B - l[0], C, cnt + 10), solve(l[1:], A, B, C - l[0], cnt + 10))

if __name__ == '__main__':
    main()
