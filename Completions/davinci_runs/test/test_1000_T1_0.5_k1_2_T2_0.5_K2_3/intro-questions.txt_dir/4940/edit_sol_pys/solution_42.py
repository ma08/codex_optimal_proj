

def main():
    n, m = map(int, input().split()) # n-number of tasks, m-number of people
    p = [list(map(int, input().split())) for _ in range(n)] # p-list of lists of time for each task and person (n x m)
    t = [0] * n # t-list of time for each task
    for i in range(n): # for each task
        for j in range(m): # for each person
            if t[i] < max(t): # if time of task is less than max time of tasks
                t[i] = max(t) # make time of task equal to max time of tasks
            t[i] += p[i][j] # time of task + time of task for person (i x j)
    print(*t) # print time of tasks

if __name__ == '__main__':
    main()
