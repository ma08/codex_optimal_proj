
def solve(n, k, a):
    a = sorted(a)
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if a[j] - a[i] <= 5:
                ans = max(ans, j - i + 1)
    return ans


if __name__ == "__main__":
    # n, k = map(int, input().split())
    # a = list(map(int, input().split()))
    n, k = 5, 3
    a = [4, 5, 1, 2, 3]
    print(solve(n, k, a))  # 4

    n, k = 7, 3
    a = [10, 9, 8, 7, 7, 7, 5]
    print(solve(n, k, a))  # 6

    n, k = 5, 2
    a = [1, 2, 1, 2, 1]
    print(solve(n, k, a))  # 3

    n, k = 5, 2
    a = [1, 2, 3, 4, 5]
    print(solve(n, k, a))  # 3

    n, k = 5, 2
    a = [1, 2, 3, 4, 4]
    print(solve(n, k, a))  # 3

    n, k = 5, 2
    a = [1, 2, 3, 4, 1]
    print(solve(n, k, a))  # 3

    n, k = 5, 2
    a = [1, 2, 3, 4, 5]
    print(solve(n, k, a))  # 3

    n, k = 5, 2
    a = [1, 2, 3, 4, 5]
    print(solve(n, k, a))  # 3

    n, k = 5, 2
    a = [1, 2, 3, 4, 5]
    print(solve(n, k, a))  # 3

    n, k = 5, 2
    a = [1, 2, 3, 4, 5]
    print(solve(n, k, a))  # 3

    n, k = 5, 2
    a = [1, 2, 3, 4, 5]
    print(solve(n, k, a))  # 3

    n, k = 5, 2
    a = [1, 2, 3, 4, 5]
    print(solve(n, k, a))  # 3

    n, k = 5, 2
    a = [1, 2, 3, 4, 5]
    print(solve(n, k, a))  # 3

    n, k = 5, 2
    a = [1, 2, 3, 4, 5]
    print(solve(n, k, a))  # 3

    n, k = 5, 2
    a = [1, 2, 3, 4, 5]
    print(solve(n, k, a))  # 3

    n, k = 5, 2
    a = [1, 2, 3, 4, 5]
    print(solve(n, k, a))  # 3

    n, k = 5, 2
    a = [1, 2, 3, 4, 5]
    print(solve(n, k, a))  # 3

    n, k = 5, 2
    a = [1, 2, 3, 4, 5]
    print(solve(n, k, a))  # 3
