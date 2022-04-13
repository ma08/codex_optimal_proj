#!/usr/bin/env python3

N, M = [int(x) for x in input().split()]

times = []
for i in range(N):
    times.append([int(x) for x in input().split()])

#print(times)

# sort the times by the first stage (1, 2, 3, 4)
times.sort(key = lambda x: x[0])

#print(times)

# sort the times by the second stage (2, 3, 4, 1)
times.sort(key = lambda x: x[1])

#print(times)

# sort the times by the third stage (3, 4, 1, 2)
times.sort(key = lambda x: x[2])

#print(times)

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
