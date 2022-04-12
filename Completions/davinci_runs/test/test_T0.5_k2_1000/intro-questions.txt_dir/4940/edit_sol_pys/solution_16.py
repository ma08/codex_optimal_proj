

def main():
    n, m = map(int, input().split()) # n: number of people, m: number of tasks
    p = [list(map(int, input().split())) for _ in range(m)] # p: time of each task
    t = [0] * m # t: time of each person
    for j in range(m): # for each task
        for i in range(m): # for each person
            if t[i] < max(t): # if the person is not the last one
                t[i] = max(t) # wait until the last person finishes the task
            t[i] += p[j][i] # the person finishes the task
    print(*t) # print the time of each person

if __name__ == '__main__':
    main()
