N, M = [int(x) for x in input().split()]

times = []
for i in range(N):
    times.append([int(x) for x in input().split()])
# sort the times by the first stage
times.sort(key = lambda x: x[0])
# sort the times by the second stage
times.sort(key = lambda x: x[1])
# sort the times by the third stage
times.sort(key = lambda x: x[2])
# now we can just add up the times
total_times = []
for i in range(N):
    total_time = 0
    for j in range(M):
        total_time += times[i][j]
    total_times.append(total_time)

for i in range(N):
    print(total_times[i], end=" ")
print()
