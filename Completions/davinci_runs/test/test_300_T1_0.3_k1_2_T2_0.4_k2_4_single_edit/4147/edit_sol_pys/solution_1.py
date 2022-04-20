import sys

def main():
    N, A, B, C = map(int, sys.stdin.readline().split())
    L = [int(sys.stdin.readline()) for _ in range(N)]
    L.sort(reverse=True)
    print(solve(L, A, B, C))

def solve(L, A, B, C):
    if L[0] >= A and L[1] >= B and L[2] >= C:
        return 0
    elif (L[0] + L[1] + L[2] >= A + B + C) and (L[0] + L[1] >= A + B or L[1] + L[2] >= B + C or L[0] + L[2] >= A + C):
        return 10
    else:
        return 10 + solve(L[1:], A - L[0], B - L[0], C - L[0])

if __name__ == '__main__':
    main()
