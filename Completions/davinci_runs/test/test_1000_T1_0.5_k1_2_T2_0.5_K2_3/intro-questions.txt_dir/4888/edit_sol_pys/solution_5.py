n, t = map(int, input().split())
tasks = list(map(int, input().split()))

tasks_done = 0
time_used = 0
for task in tasks:
    if time_used + task <= t:
        time_used += task
        tasks_done += 1
    else:
        break

print(tasks_done)
