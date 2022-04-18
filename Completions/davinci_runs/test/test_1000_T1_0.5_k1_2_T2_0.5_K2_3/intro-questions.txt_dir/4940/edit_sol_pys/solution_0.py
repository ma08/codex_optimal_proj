

def main():
    n, m = map(int, input().split())  # n-number of tasks, m-number of people
    p = [list(map(int, input().split())) for _ in range(n)]  # p-list of lists of time for each task and person
    t = [0] * n  # t-list of time for each task
    for j in range(m):  # for each person
        for i in range(n):  # for each task
            if t[i] < max(t):  # if time of task is less then max time of tasks
                t[i] = max(t)  # make time of task equal max time of tasks
            t[i] += p[i][j]  # time of task + time of task for person
    print(*t)  # print time of tasks

if __name__ == '__main__':
    main()
