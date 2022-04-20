

# n = int(input())
# a = [list(map(int, input().split())) for i in range(n)]

def main():
    n = int(input())
    a = [list(map(int, input().split())) for i in range(n)]
    # a = [[3, 5], [1, 4], [2, 4], [1, 5], [2, 3]]
    # a = [[2, 3], [3, 1], [1, 2]]
    # a = [[2, 3], [3, 1], [1, 2]]

    # print(a)

    # start = a[0][0]
    # end = a[0][1]

    # for i in range(n):
    #     for j in range(n):
    #         if a[i][0] == start:
    #             print(i, j)
    #             start = a[i][1]
    #             end = a[i][0]

    # print(a)

    p = [0] * n
    p[0] = a[0][0]
    p[1] = a[0][1]

    for i in range(2, n):
        for j in range(n):
            if a[j][0] == p[i - 1]:
                p[i] = a[j][1]
                break
            elif a[j][1] == p[i - 1]:
                p[i] = a[j][0]
                break

    print(*p)

if __name__ == "__main__":
    main()