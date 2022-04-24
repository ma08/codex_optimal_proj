

def main():
    n = int(input())
    a = [None] * n
    for i in range(n):
        a[i] = list(map(lambda x: int(x) - 1, input().split()))
    for i in range(n):
        if a[i][0] == i:
            a[i] = a[i][1]
        else:
            a[i] = a[i][0]
    for i in range(n):
        j = a[i]
        a[i] = a[j]
        a[j] = i
    ans = [0] * n
    for i in range(n):
        ans[i] = a[i] + 1
    print(*ans)


if __name__ == '__main__':
    main()
