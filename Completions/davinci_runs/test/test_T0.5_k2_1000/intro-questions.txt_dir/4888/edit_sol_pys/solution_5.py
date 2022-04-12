

def main():
    # Get inputs
    n, t = [int(x) for x in input().split()]  # n = number of tasks, t = time limit
    times = [int(x) for x in input().split()]  # times = list of task times
    # Iterate through tasks and see if they can be completed
    total = 0
    for time in times:
        total += time
        if total > t:
            print(times.index(time))  # print the index of the task that was not completed
            break
    else:
        print(n)  # if all tasks are completed, print n

if __name__ == '__main__':
    main()
