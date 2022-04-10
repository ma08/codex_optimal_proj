


def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l.sort(key=lambda x: x[1])
    ans = l[0][1] - l[0][0]
    for i in range(1, n):
        if l[i][1] - l[i][0] > ans:
            ans = l[i][1] - l[i][0]
        if l[i][1] - l[i][0] < l[i][1] - l[i - 1][0]:
            ans = l[i][1] - l[i - 1][0]
    print(ans)


if __name__ == "__main__":
    main()