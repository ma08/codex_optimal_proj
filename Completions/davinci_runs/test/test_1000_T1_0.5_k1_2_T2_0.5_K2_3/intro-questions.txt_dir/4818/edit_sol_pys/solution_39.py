

def main():
    # Read in the first line of input and split it into two numbers
    # n and m
    n, m = input().split()

    # Convert the two numbers to integers
    n = int(n)
    m = int(m)

    # Read in the next n lines and split them into two numbers
    # a and b
    tasks = [input().split() for i in range(n)]

    # Convert the two numbers to integers
    for i in range(n):
        tasks[i][0] = int(tasks[i][0])
        tasks[i][1] = int(tasks[i][1])

    # Read in the next m lines and split them into two numbers
    # x and y
    quiet = [input().split() for i in range(m)]

    # Convert the two numbers to integers
    for i in range(m):
        quiet[i][0] = int(quiet[i][0])
        quiet[i][1] = int(quiet[i][1])

    # Sort the tasks and quiet intervals
    tasks = sorted(tasks, key=lambda x: x[1])
    quiet = sorted(quiet, key=lambda x: x[1])

    # Keep track of the number of tasks completed
    completed = 0

    # Keep track of the time of the last quiet interval
    lastQuiet = 0

    # Go through each task
    for task in tasks:
        # Go through each quiet interval
        for i in range(lastQuiet, m):
            # Check if the task can be completed in this quiet interval
            if task[0] <= quiet[i][0] and task[1] >= quiet[i][1]:
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
