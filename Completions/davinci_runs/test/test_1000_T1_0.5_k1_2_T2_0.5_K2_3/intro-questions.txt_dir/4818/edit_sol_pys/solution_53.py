

def main():
    # Reads in the input
    n, m = map(int, raw_input().split(' '))
    tasks = list(map(int, raw_input().split(' ')))
    quiet = list(map(int, raw_input().split(' ')))

    # Sorts the tasks and quiet intervals
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
    print(completed)

if __name__ == "__main__":
    main()
