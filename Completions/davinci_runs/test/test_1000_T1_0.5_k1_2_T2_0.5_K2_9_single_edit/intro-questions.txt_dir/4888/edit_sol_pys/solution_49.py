

n, t = map(int, input().split()) #n number of tasks, t time limit
tasks = list(map(int, input().split())) #tasks in minutes

tasks_done = 0
time_used = 0
for task in tasks:
    if time_used + task <= t:
        time_used += task
        tasks_done += 1
    else:
        break

print(tasks_done)
