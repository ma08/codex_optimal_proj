import sys
sys.setrecursionlimit(2**20)


    if n == 1:
        return 1
def solve(n, q):
    p = [1]
    for i in range(n - 2):
        if p[-1] + q[i] > 0 and p[-1] + q[i] <= n - 1:
            p.append(p[-1] + q[i] + 1)
        else:
            return [-1]
    if p[-1] + q[-1] == n:
        p.append(p[-1] + q[-1])
    else:
        return [-1]
    return p


def main():
    n = int(input())
    q = list(map(int, input().split()))
    print(*solve(n, q))


if __name__ == "__main__":
    main()
