
# coding: utf-8

def main():
    n, m = map(int, input().split())
    exams = []
    for _ in range(m):
        exams.append(tuple(map(int, input().split())))

    days = [0] * n
    for exam in exams:
        s, f, c = exam
        if c > f - s:
            print(-1)
            return
        days[s] += 1
        days[f] -= 1

    for j in range(1, n):
        days[j] += days[j - 1]
        if days[i] > 1:
            print(-1)
            return

    days = [0] * n
    for exam in exams:
        s, f, c = exam
        for j in range(s, f):
            days[j] = c
        c -= 1
        for j in range(s - 1, -1, -1):
            if days[j] == 0:
                days[j] = c
                c -= 1
                if c == 0:
                    break

    for j in range(n - 1, -1, -1):
        if days[j] == 0:
            days[j] = m + 1
        elif days[j] != m + 1:
            days[j] -= 1
    
    print(' '.join(map(str, days)))


if __name__ == "__main__":
    main()
