

from collections import defaultdict

def solve(n, m, a):
    d = defaultdict(int)
    for i in range(n):
        for j in range(m):
            d[(i, j)] = a[i][j]
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                d[(i, j)] = 0
            else:
                d[(i, j)] = min(d[(i-1, j)], d[(i, j-1)], d[(i-1, j-1)]) + 1 if i > 0 and j > 0 else 1
    return sum(d.values())

def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    print(solve(n, m, a))

if __name__ == "__main__":
    main()
