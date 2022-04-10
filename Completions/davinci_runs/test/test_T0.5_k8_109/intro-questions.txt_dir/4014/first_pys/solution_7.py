

def main():
    n, m = [int(i) for i in input().split()]
    exams = []
    for i in range(m):
        exams.append([int(i) for i in input().split()])
    exams.sort()
    days = [0] * n
    for i in range(len(exams)):
        s, d, c = exams[i]
        if days[s-1] == 0:
            days[s-1] = i+1
            c -= 1
        if c > 0:
            for j in range(s, d):
                if days[j] == 0:
                    days[j] = i+1
                    c -= 1
                if c == 0:
                    break
        if c > 0:
            print("-1")
            return
    for i in range(len(days)):
        if days[i] != 0:
            days[i] = m+1
    print(" ".join([str(i) for i in days]))
    return

main()