def main():
    n, m = map(int, input().split())
    exams = []
    for i in range(m):
        exams.append(list(map(int, input().split())))
    exams.sort(key=lambda x: x[1])


    ans = [m + 1] * n
    for i in range(m):
        for j in range(exams[i][0], exams[i][1]):
            if ans[j] == m + 1:
                ans[j] = i + 1

    if ans.count(m + 1) > 0:
        print(-1)
    else:
        print(*ans)


if __name__ == "__main__":
    main()
