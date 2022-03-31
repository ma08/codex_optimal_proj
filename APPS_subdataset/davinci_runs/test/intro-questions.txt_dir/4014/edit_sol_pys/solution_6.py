

def main():
    n, m = map(int, input().split())
    exams = []
    for i in range(m):
        exams.append(list(map(int, input().split())))
    exams.sort(key=lambda x: x[1])
    res = [0] * n
    for exam in exams:
        s, d, c = exam[1:]
        if s + c > n:
            print(-1)
            return
        if s + c > d:
            print(-1)
            return
        for i in range(s, s + c):
            if res[i] != 0:
                print(-1)
                return
            res[i] = exam[1]
        res[d - 1] = m + 1
    print(' '.join(map(str, res)))


if __name__ == '__main__':
    main()
