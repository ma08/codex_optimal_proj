

import re
import sys

def main():
    n, m = map(int, input().split())
    exams = []
    for _ in range(m):
        exams.append(tuple(map(int, input().split())))

    days = [0] * n
    for exam in exams:
        s, t, c = exam
        if c > t - s:
            print(-1)
            return
        days[s] += 1
        days[t] -= 1

    for i in range(1, n):
        days[i] += days[i - 1]
        if days[i] > 1:
            print(-1)
            return

    days = [0] * n
    for exam in exams:
        s, t, c = exam
        for i in range(s, t):
            days[i] = c
        c -= 1
        for i in range(s - 1, -1, -1): # s - 1 because we already did s
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
