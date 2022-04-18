


def main():
    # Get input
    n, t = [int(x) for x in input().split()] # n is the number of tasks, t is the time limit
    times = [int(x) for x in input().split()] # times is a list of the time each task takes
    # Iterate through tasks and see if they can be completed
    total = 0
    for time in times:
        total += time
        if total > t:
            print(times.index(time)) # the index of the task that was started but not completed
            break
    else:
        print(n) # all tasks were completed


if __name__ == '__main__':
    main()
