
# solve

def solve(n, a, b, c, d):
    a_sorted = sorted(a + c)
    b_sorted = sorted(b + d)
    res = 0
    for i in range(n):
        res += a_sorted[i] * b_sorted[n - i - 1]
    return res


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))
    print(solve(n, a, b, c, d))


if __name__ == "__main__":
    main()
