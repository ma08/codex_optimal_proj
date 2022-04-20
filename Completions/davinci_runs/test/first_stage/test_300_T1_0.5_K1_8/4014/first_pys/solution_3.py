

def main():
    """
    思路：从第一天开始，遍历每一天，每一天只能有一个活动，即考试、休息、准备考试，其中考试日期和准备考试日期都是已知的，
    只要每天只有一个活动，然后把每天的活动记录下来，最后看每一个考试是否都可以准备好。
    """
    n, m = map(int, input().split())
    days = [0] * n
    for i in range(m):
        s, d, c = map(int, input().split())
        for j in range(s-1, d-1):
            if days[j] == 0:
                days[j] = c
            elif days[j] != c:
                print(-1)
                return

    for i in range(n):
        if days[i] == 0:
            days[i] = m+1
        else:
            days[i] = days[i]
    print(*days)


if __name__ == "__main__":
    main()