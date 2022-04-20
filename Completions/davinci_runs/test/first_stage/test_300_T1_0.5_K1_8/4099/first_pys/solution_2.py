


def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    if n*m <= sum_a:
        print(0)
    else:
        print(n*m-sum_a) if n*m-sum_a <= k else print(-1)


if __name__ == "__main__":
    main()