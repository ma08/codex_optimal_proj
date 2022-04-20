

if __name__ == "__main__":
    n, m = map(int, input().split())
    result = [0] * n
    exams = []
    for i in range(m):
        s, d, c = map(int, input().split())
        exams.append((s, d, c))
    exams.sort(key=lambda x: x[1])
    for i in range(m):
        s, d, c = exams[i]
        days_left = c
        for j in range(s - 1, d):
            if result[j] == 0:
                result[j] = i + 1
                days_left -= 1
        if days_left > 0:
            print(-1)
            exit()
    for i in range(m):
        s, d, c = exams[i]
        for j in range(s - 1, d):
            if result[j] == i + 1:
                result[j] = m + 1
    print(*result)