

# Read input:
n, T = map(int, input().split())
tasks = list(map(int, input().split()))

# Solve problem:
completed = 0
time = 0
for t in tasks:
    if time + t <= T:
        time += t
        completed += 1
    else:
        break

# Print output:
print(completed)
