
n, t = map(int, input().split())
tasks = list(map(int, input().split()))

tasks_done = 0
time_spent = 0
for task in tasks:
    if time_spent + task <= t:
        time_spent += task
        tasks_done += 1
    else:
        break

print(tasks_done)
