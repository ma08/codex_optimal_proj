

def solve(n, m, a):
    return n * m - sum(a)


if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, m, a))
