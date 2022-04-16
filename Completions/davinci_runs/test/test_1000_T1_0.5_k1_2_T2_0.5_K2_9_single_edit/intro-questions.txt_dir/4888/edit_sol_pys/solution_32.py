

def main():
    # Get input
    n, t = [int(x) for x in input().split()] # n = number of tasks, t = time limit
    times = [int(x) for x in input().split()] # times = list of time it takes to complete each task
    # Iterate through tasks and see if they can be completed
    total = 0
    for time in times:
        total += time
        if total > t:
            print(times.index(time)) # index of the task that will not be completed
            break
    else:
        print(n)

if __name__ == '__main__':
    main()
