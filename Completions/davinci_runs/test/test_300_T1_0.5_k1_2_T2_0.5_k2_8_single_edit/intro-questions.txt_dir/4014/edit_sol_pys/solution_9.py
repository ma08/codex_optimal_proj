#!/usr/bin/env python3

import re
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    exams = []
    for _ in range(m):
        exams.append(tuple(map(int, sys.stdin.readline().split())))

    days = [0] * n
    for exam in exams:
        s, f, c = exam
        if c > f - s:
            print(-1, file=sys.stdout)
            return
        days[s] += 1
        days[f] -= 1

    for i in range(1, n):
        days[i] += days[i - 1]
        if days[i] > 1:
            print(-1, file=sys.stdout)
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
    
    print(' '.join(map(str, days)), file=sys.stdout)


if __name__ == "__main__":
    main()
