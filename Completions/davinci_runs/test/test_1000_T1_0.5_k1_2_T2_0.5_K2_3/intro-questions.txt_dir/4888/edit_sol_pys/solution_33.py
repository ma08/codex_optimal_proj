
import sys

# Read input
n, T = map(int, sys.stdin.readline().split())
tasks = list(map(int, sys.stdin.readline().split()))

# Solve
completed = 0
time = 0
for task in tasks:
    if time + task <= T:
        time += task
        completed += 1
print(completed)
