import sys
n, t = map(int, sys.stdin.readline().split())
tasks = list(map(int, sys.stdin.readline().split()))

tasks_done = 0 # number of tasks done
time_used = 0
for task in tasks:
    if time_used + task <= t:
        time_used += task
        tasks_done += 1
    else:
        break

print(tasks_done)
