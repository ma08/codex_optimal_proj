
def main():
    n = int(input())
    a = [[] for _ in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))[1:]
    for i in range(n):
        for j in range(len(a[i])):
            a[i][j] -= 1
    for i in range(n):
        for j in range(len(a[i])):
            k = a[i][j]
            a[k].append(i)
    ans = [0] * n
    for i in range(n):
        ans[i] = i + 1
    for i in range(n):
        for j in range(len(a[i])):
            k = a[i][j]
            ans[i], ans[k] = ans[k], ans[i]
    print(*ans)


if __name__ == '__main__':
    main()
