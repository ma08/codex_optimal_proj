
def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    ans = 0



    # for i in range(n):
    #     for j in range(n):
    #         if i == j:
    #             continue
    #         else:
    #             ans += abs(xy[i][0] - xy[j][0]) + abs(xy[i][1] - xy[j][1])
    # print(ans // 2)


if __name__ == '__main__':
    main()
