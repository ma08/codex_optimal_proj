

def main():
    n, m = map(int, input().split())
    exams = []
    for _ in range(m):
        exams.append(list(map(int, input().split())))
    exams.sort(key=lambda x: x[1])
    schedule = [0] * n
    for exam in exams:
        s, d, c = exam[0], exam[1], exam[2]
        if d - s < c:
            print(-1)
            return
        for i in range(s, d):
            if schedule[i] != 0:
                print(-1)
                return
        for i in range(c):
            schedule[s + i] = exam[3]
        schedule[d - 1] = m + 1
    print(*schedule)

if __name__ == "__main__":
    main()
