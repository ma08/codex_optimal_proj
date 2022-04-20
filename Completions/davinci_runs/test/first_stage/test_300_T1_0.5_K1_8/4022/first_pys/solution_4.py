


def main():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    a.sort()
    b = [0] * n
    for i in range(n):
        b[i] = a[i][1] - a[i][0]
    s = sum(b)
    m = max(b)
    print(s - m)


if __name__ == "__main__":
    main()