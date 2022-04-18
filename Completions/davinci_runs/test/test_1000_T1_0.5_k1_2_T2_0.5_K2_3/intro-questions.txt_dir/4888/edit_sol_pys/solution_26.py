n, t = map(int, input().split())
tasks = list(map(int, input().split()))

cur_time = 0
for i in range(n):
    cur_time += tasks[i]
    if cur_time > t:
        break
    else:
        tasks_done = i + 1

print(tasks_done)
