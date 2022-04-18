

def solve(n, a, b):
    a_sorted = sorted(a)
    b_sorted = sorted(b)
    res = 0
    for i in range(n):
        res += a_sorted[i] * b_sorted[n - i - 1]
    return res


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(n, a, b))


if __name__ == "__main__":
    main()
