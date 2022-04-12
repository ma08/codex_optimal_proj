
def main():
    n = int(input())
    a = [0] * n
    for i in range(n):
        a[i] = int(input()) - 1
    for i in range(n):
        if a[a[i]] == i:
            a[i] = -1
    for i in range(n - 1, -1, -1):
        if a[i] == -1:
            a.pop(i)
    n = len(a)
    ans = [0] * n
    for i in range(n):
        ans[i] = i + 1
    for i in range(n):
        j = a[i]
        ans[i], ans[j] = ans[j], ans[i]
    print(*ans)


if __name__ == '__main__':
    main()
