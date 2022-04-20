

def main():
    n, m = map(int, input().split())
    exams = []
    for _ in range(m):
        s, d, c = map(int, input().split())
        exams.append((s, d, c))
    exams.sort()
    ans = [0] * n
    for i, exam in enumerate(exams):
        s, d, c = exam
        if d - s < c:
            return -1
        for j in range(s, d - c):
            if ans[j] == 0:
                ans[j] = i + 1
            else:
                return -1
        for j in range(d - c, d):
            if ans[j] == 0:
                ans[j] = m + 1
            else:
                return -1
    return ' '.join(map(str, ans))

print(main())