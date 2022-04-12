n, T = map(int, input().split())
tasks = map(int, input().split())

count = 0
time = 0
for i in range(n):
    if time + tasks[i] <= T:
        count += 1
        time += tasks[i]
    else:
        break

print(count)
