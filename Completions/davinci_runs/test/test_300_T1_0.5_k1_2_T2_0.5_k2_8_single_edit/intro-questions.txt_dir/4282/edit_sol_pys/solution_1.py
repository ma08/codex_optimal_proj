


def main():
    n = int(input())
    a = [[0] for _ in range(n)]
    for i in range(n):
        a[i] = int(input())
    for i in range(n - 1):
        j = a[i] - 1
        a[i], a[j] = a[j], a[i]
    ans = [0] * n
    for i in range(n):
        ans[i] = i + 1
    print(*ans)


if __name__ == '__main__':
    main()
