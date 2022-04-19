

def main():
    n, m = map(int, input().split())
    exams = []
    for _ in range(m):
        exams.append(list(map(int, input().split())))
    exams.sort(key=lambda x: x[1])
    schedule = [0] * n
    for exam in exams:
        s, d, c = exam
        if d - s < c:
            print(-1)
            return
        for i in range(s - 1, d):
            if schedule[i] != 0 and schedule[i] != m + 1:
                print(-1)
                return
        for i in range(c):
            schedule[s - 1 + i] = exam[0]
        schedule[d - 1] = m + 1
    print(*schedule)

if __name__ == "__main__":
    main()
