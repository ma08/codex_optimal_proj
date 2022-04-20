

def main():
    n, m = map(int, input().split())
    exams = []
    for _ in range(m):
        s, d, c = map(int, input().split())
        exams.append((s, d, c))

    exams.sort()
    schedule = [0] * n
    for s, d, c in exams:
        for i in range(s, d):
            if schedule[i]:
                print(-1)
                return
            schedule[i] = c

    print(*schedule)


if __name__ == "__main__":
    main()