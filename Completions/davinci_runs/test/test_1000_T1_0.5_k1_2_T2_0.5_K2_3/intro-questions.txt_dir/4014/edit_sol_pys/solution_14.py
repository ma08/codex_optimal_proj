
def main():
    n, m = map(int, input().split())  # n: number of days, m: number of exams
    exams = []
    for _ in range(m):
        exams.append(tuple(map(int, input().split())))

    days = [0] * n
    for exam in exams:
        s, f, c = exam  # s: start day, f: finish day, c: number of days to finish
        if c > f - s:  # invalid exam
            print(-1)
            return
        days[s] += 1  # add 1 to the start day
        # if the number of exams scheduled on the ith day is greater than 1,
        # it is invalid
        days[f] -= 1  # subtract 1 from the finish day

    for i in range(1, n):
        days[i] += days[i - 1]
        if days[i] > 1:
            print(-1)
            return

    days = [0] * n
    for exam in exams:
        s, f, c = exam
        for i in range(s, f):
            days[i] = c
        c -= 1
        for i in range(s - 1, -1, -1):
            if days[i] == 0:
                days[i] = c
                c -= 1
                if c == 0:
                    break

    for i in range(n - 1, -1, -1):
        if days[i] == 0:
            days[i] = m + 1
        elif days[i] != m + 1:
            days[i] -= 1
    
    print(' '.join(map(str, days)))


if __name__ == "__main__":
    main()
