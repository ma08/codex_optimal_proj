

def main():
    n, m = map(int, input().split())
    exams = []
    for _ in range(m):
        exams.append(tuple(map(int, input().split())))

    days = [0] * n
    for exam in exams:
        start, end, count = exam
        if count > end - start:
            print(-1)
            return
        days[start] += 1
        days[end] -= 1

    for i in range(1, n):
        days[i] += days[i - 1]
        if days[i] > 1:
            print(-1)
            return

    days = [0] * n
    for exam in exams:
        start, end, count = exam
        for i in range(start, end):
            days[i] = count
        count -= 1
        for i in range(start - 1, -1, -1):
            if days[i] == 0:
                days[i] = count
                count -= 1
                if count == 0:
                    break

    for i in range(n - 1, -1, -1):
        if days[i] == 0:
            days[i] = m + 1
        elif days[i] != m + 1:
            days[i] -= 1
    
    print(' '.join(map(str, days)))


if __name__ == "__main__":
    main()
