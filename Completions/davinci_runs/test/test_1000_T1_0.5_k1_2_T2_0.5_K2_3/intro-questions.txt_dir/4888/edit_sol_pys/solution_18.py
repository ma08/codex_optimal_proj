n, T = map(int, input().split())
times = list(map(int, input().split()))

curr_time = 0
num_tasks = 0

for i in range(n + 1):
    if curr_time + times[i] > T:
        break
    curr_time += times[i]
    num_tasks += 1

print(num_tasks)
