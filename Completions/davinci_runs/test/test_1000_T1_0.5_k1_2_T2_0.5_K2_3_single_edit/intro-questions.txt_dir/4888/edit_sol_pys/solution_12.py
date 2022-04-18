n, T = map(int, input().split())


times = [0]
times += list(map(int, input().split()))

num_tasks = 1
curr_time = times[1]
for i in range(2, n + 1):
    if curr_time + times[i] > T:
        break 
    num_tasks += 1
    curr_time += times[i]

print(num_tasks)
