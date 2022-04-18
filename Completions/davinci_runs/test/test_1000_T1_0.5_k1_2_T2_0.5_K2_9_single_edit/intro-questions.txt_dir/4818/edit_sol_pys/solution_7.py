

def main(n, m, tasks, quiet):
    # # Read in the input
    # n, m = map(int, input().split(' '))
    # tasks = list(map(int, input().split(' ')))
    # quiet = list(map(int, input().split(' ')))

    # Sort the tasks and quiet intervals
    tasks.sort()
    quiet.sort()

    # Keep track of the number of tasks completed
    completed = 0

    # Keep track of the time of the last quiet interval
    lastQuiet = 0

    # Go through each task
    for task in tasks:
        # Go through each quiet interval
        for i in range(lastQuiet, m):
            # Check if the task can be completed in this quiet interval
            if task <= quiet[i]:
                # Increment the number of tasks completed
                completed += 1

                # Update the last quiet interval
                lastQuiet = i + 1

                # Move onto the next task
                break

    # Print out the number of tasks completed
    return completed

if __name__ == "__main__":
    n, m = map(int, input().split(' '))
    tasks = list(map(int, input().split(' ')))
    quiet = list(map(int, input().split(' ')))
    print(main(n, m, tasks, quiet))
