
def main():
    n, m = map(int, input().split())
    exams = []
    for _ in range(m):
        exams.append(list(map(int, input().split())))
    exams.sort(key=lambda x: x[1])
    schedule = [0] * n
    for exam in exams:
        start, end, count = exam
        if end - start < count:
            print(-1)
            return
        for i in range(start, end):
            if schedule[i] != 0:
                print(-1)
                return
            schedule[start + i] = exam[0]
        schedule[end - 1] = m + 1
    print(*schedule)

if __name__ == "__main__":
    main()
