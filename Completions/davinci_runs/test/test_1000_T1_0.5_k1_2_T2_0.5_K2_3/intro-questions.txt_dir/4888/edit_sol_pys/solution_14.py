# Read input
n, T = map(int, input().split())
tasks = list(map(int, input().split()))

# Solve
completed = 0
time = 0
for task in tasks:
    if time + task <= T:
        time += task
        completed += 1
print(completed)
