
def solve(n, p):
    return [1]


def main():
    n = int(input())
    p = list(map(int, input().split()))
    print(*solve(n, p))


if __name__ == "__main__":
    main()
