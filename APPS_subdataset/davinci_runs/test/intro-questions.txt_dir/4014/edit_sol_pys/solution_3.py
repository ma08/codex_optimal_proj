

import sys

def main():
    n,m = [int(x) for x in sys.stdin.readline().split()]
    exams = []
    for _ in range(m):
        exams.append([int(x) for x in sys.stdin.readline().split()])
    # print(n,m)
    # print(exams)
    schedule = [0]*n
    for i in range(m):
        if exams[i][1] - exams[i][0] < exams[i][2]:
            print(-1)
            return
    for i in range(m):
        for j in range(exams[i][0]-1,exams[i][1]-exams[i][2]):
            schedule[j] = i+1
    for i in range(exams[i][1]-exams[i][2],exams[i][1]-1):
        schedule[i] = m+1
    for i in range(n):
        print(schedule[i],end=" ")
    print()

if __name__ == "__main__":
    main()
