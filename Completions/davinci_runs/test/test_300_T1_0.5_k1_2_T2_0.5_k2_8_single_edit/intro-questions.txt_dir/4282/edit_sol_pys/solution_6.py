


def main():
    n = int(input())
    a = [[] for _ in range(n + 1)]
    for i in range(n):
        a[i + 1] = list(map(int, input().split()))
    for i in range(n):
        a[i + 1][0] -= 1
        a[i + 1][1] -= 1
    for i in range(n):
        if len(a[i + 1]) == 2:
            j = a[i + 1][0]
            if a[j + 1][0] == i:
                a[j + 1][0] = a[j + 1][1]
                a[j + 1].pop()
            else:
                a[j + 1][1] = a[j + 1][0]
                a[j + 1][0] = i
            if a[j + 1][0] == j:
                a[j + 1].pop()
            a[i + 1].pop()
    for i in range(n):
        a[i + 1] = a[i + 1][0]
    ans = [0] * n
    for i in range(n):
        ans[i] = i + 1
    for i in range(n):
        j = a[i + 1]
        ans[i], ans[j + 1] = ans[j + 1], ans[i]
    print(*ans)


if __name__ == '__main__':
    main()
