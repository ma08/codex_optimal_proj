


def main():
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    # s = [0] * (n + 1)
    # for i in range(n):
    #     s[i + 1] = s[i] + a[i]

    # print(s)

    # d = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    # for l in range(1, n + 1):
    #     for r in range(l, n + 1):
    #         # print(l, r)
    #         if r - l + 1 == 2:
    #             if a[l - 1] == m:
    #                 d[2] += 1
    #         elif r - l + 1 == 3:
    #             if a[l - 1] == m or a[r - 1] == m or (a[l - 1] + a[r - 1]) // 2 == m:
    #                 d[3] += 1
    #         elif r - l + 1 == 4:
    #             if a[l - 1] == m or a[r - 1] == m or (a[l - 1] + a[r - 1]) // 2 == m:
    #                 d[4] += 1
    #         elif r - l + 1 == 5:
    #             if a[l - 1] == m or a[r - 1] == m or (a[l - 1] + a[r - 1]) // 2 == m:
    #                 d[5] += 1
    #         else:
    #             if a[l - 1] == m or a[r - 1] == m or (a[l - 1] + a[r - 1]) // 2 == m:
    #                 d[6] += 1

    # print(d)

    d = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in range(1, n + 1):
        if a[i - 1] == m:
            d[2] += i
            d[3] += i * (i - 1) // 2
            d[4] += i * (i - 1) * (i - 2) // 6
            d[5] += i * (i - 1) * (i - 2) * (i - 3) // 24
            d[6] += i * (i - 1) * (i - 2) * (i - 3) * (i - 4) // 120

    print(d)
    print(d[2] + d[3] + d[4] + d[5] + d[6])

    # res = 0
    # for l in range(1, n + 1):
    #     for r in range(l, n + 1):
    #         if r - l + 1 == 2:
    #             if a[l - 1] == m:
    #                 res += 1
    #         elif r - l + 1 == 3:
    #             if a[l - 1] == m or a[r - 1] == m or (a[l - 1] + a[r - 1]) // 2 == m:
    #                 res += 1
    #         elif r - l + 1 == 4:
    #             if a[l - 1] == m or a[r - 1] == m or (a[l - 1] + a[r - 1]) // 2 == m:
    #                 res += 1
    #         elif r - l + 1 == 5:
    #             if a[l - 1] == m or a[r - 1] == m or (a[l - 1] + a[r - 1]) // 2 == m:
    #                 res += 1
    #         else:
    #             if a[l - 1] == m or a[r - 1] == m or (a[l - 1] + a[r - 1]) // 2 == m:
    #                 res += 1

    # print(res)


if __name__ == '__main__':
    main()