


def max_beauty_sum(n, k, x, a):
    if x < n - k + 1:
        return -1
    elif x == n - k + 1:
        return sum(a[i] for i in range(k - 1, n))
    else:
        return sum(a)


def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(max_beauty_sum(n, k, x, a))


if __name__ == "__main__":
    main()