# Read input
n, T = map(int, input().split())  # n = number of tasks, T = time limit
tasks = list(map(int, input().split()))  # list of tasks

# Solve
completed = 0  # number of completed tasks
time = 0  # time spent on completed tasks
for task in tasks:
    if time + task <= T:
        time += task
        completed += 1

print(completed)
