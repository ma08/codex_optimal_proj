

# Read input
n, T = map(int, input().split()) # n = number of tasks, T = time limit
tasks = list(map(int, input().split())) # tasks = a list of time needed to complete each task

# Solve problem
completed = 0 # number of tasks completed
time = 0 # time spent
for t in tasks:
    if time + t <= T:
        time += t
        completed += 1
    else:
        break

# Print output
print(completed)
