
import sys

def main():
    N, A, B, C = map(int, sys.stdin.readline().split())
    l = [int(sys.stdin.readline()) for _ in range(N)]
    l.sort(reverse=True)
    print(solve(l, A, B, C))

def solve(l, A, B, C):
    if len(l) == 0:
        return float('inf')
    else:
        return min(solve(l[1:], A, B, C), 10 + solve(l[1:], A - l[0], B - l[0], C - l[0]))

if __name__ == '__main__':
    main()
