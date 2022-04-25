
def main():
    n = int(input())
    a = [[[] for _ in range(2)] for _ in range(n)]
    for i in range(n):
        a[i][0], a[i][1] = map(int, input().split())
    for i in range(n):
        if a[i][0] != -1:
            a[i][0] -= 1
            j = a[i][0]
            a[i][0] = a[j][0]
            a[j][0] = i
        if a[i][1] != -1:
            a[i][1] -= 1
            j = a[i][1]
            a[i][1] = a[j][0]
            a[j][0] = i
    ans = [0] * n
    for i in range(n):
        ans[i] = i + 1
    for i in range(n):
        if a[i][0] != -1:
            j = a[i][0]
            ans[i], ans[j] = ans[j], ans[i]
        if a[i][1] != -1:
            j = a[i][1]
            ans[i], ans[j] = ans[j], ans[i]
    print(*ans)


if __name__ == '__main__':
    main()
