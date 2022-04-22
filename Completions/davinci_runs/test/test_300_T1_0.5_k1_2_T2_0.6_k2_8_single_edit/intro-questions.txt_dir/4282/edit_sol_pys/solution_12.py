


def main():
    n = int(input())
    a = [[i] for i in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    for i in range(n):
        a[i][0] -= 1  # 0-indexed
        a[i][1] -= 1  # 0-indexed
    for i in range(n):
        if len(a[i]) == 2:  # i is a root
            j = a[i][0]
            if a[j][0] == i:  # j is the left child of i
                a[j][0] = a[j][1]
                a[j].pop()
            else:  # j is the right child of i
                a[j][1] = a[j][0]
                a[j][0] = i
            if a[j][0] == j:  # j has no child
                a[j].pop()
            a[i].pop()
    ans = [0] * n
    for i in range(n):
        ans[i] = i + 1  # 1-indexed
    for i in range(n):
        j = a[i]
        ans[i], ans[j] = ans[j], ans[i]
    print(*ans)


if __name__ == '__main__':
    main()
