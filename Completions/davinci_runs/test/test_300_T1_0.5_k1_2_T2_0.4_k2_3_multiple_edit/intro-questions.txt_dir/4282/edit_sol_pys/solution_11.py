
#

def main():
    n = int(input())
    a = [[] for _ in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))[1:]
    for i in range(n):
        for j in range(len(a[i])):
            a[i][j] -= 1
    for i in range(n):
        for j in a[i]:
            a[j].remove(i)
    for i in range(n):
        if len(a[i]) == 1:
            a[i] = a[i][0]
        else:
            a[i] = -1
    ans = [0] * n
    for i in range(n):
        ans[i] = i + 1
    for i in range(n):
        j = a[i]
        ans[i], ans[j] = ans[j], ans[i]
    print(*ans)


if __name__ == '__main__':
    main()
