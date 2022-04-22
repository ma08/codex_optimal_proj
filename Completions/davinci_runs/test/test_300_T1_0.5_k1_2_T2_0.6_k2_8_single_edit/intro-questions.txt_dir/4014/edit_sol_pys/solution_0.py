

import re
import sys

def main():
    n, m = list(map(int, input().split()))
    exams = []
    for _ in range(m):
        exams.append(list(map(int, input().split())))

    days = [0] * n
    for i, exam in enumerate(exams):
        s, f, c = exam[0], exam[1], exam[2]
        if c > f - s:
            print(-1)
            return
        days[s] += 1
        days[f] -= 1

    for i in range(1, n):
        days[i] += days[i - 1]
        if days[i] > 1:
            print(-1)
            return

    days = [0] * n
    for exam in exams:
        s, f, c = exam
        for i in range(s, f):
            days[i] = c + 1
        c -= 1
        for i in range(s - 1, -1, -1):
            if days[i] == 0:
                days[i] = c + 1
                c -= 1
                if c == 0:
                    break

    for i in range(n - 1, -1, -1):
        if days[i] == 0:
            days[i] = m + 1
        elif days[i] != m + 1:
            days[i] = days[i] - 1
    
    print(' '.join(list(map(str, days))))


if __name__ == "__main__":
    main()
