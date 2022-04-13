

def main():
    # Reads in the input
    n, m = map(int, input().split(' ')) # n = number of tasks, m = number of quiet intervals
    tasks = list(map(int, input().split(' '))) # list of tasks
    quiet = list(map(int, input().split(' '))) # list of quiet intervals

    # Sorts the tasks and quiet intervals in ascending order
    tasks.sort()
    quiet.sort()

    # Keep track of the number of tasks completed in the quiet intervals
    completed = 0

    # Keep track of the index of the last quiet interval
    lastQuiet = 0

    # Go through each task in the task list
    for task in tasks:
        # Go through each quiet interval in the quiet interval list
        for i in range(lastQuiet, m):
            # Check if the task can be completed in this quiet interval (the task should be finished before the quiet interval ends)
            if task <= quiet[i]:
                # Increment the number of tasks completed in the quiet intervals
                completed += 1

                # Update the index of the last quiet interval
                lastQuiet = i + 1

                # Move onto the next task in the task list
                break

    # Print out the number of tasks completed in the quiet intervals
    print(completed)

if __name__ == "__main__":
    main()
