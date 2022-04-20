

def main():
    n, m = map(int, input().split())
    exams = []
    for _ in range(m):
        exams.append(list(map(int, input().split())))
    exams.sort(key=lambda x: x[1])
    days = [0] * n
    for exam in exams:
        days[exam[1]-1] = m + 1
        for i in range(exam[0] - 1, exam[0] + exam[2] - 1):
            if days[i] == 0:
                days[i] = exam[0]
            else:
                if days[i] != exam[0]:
                    print(-1)
                    return
    print(' '.join(map(str, days)))

if __name__ == '__main__':
    main()