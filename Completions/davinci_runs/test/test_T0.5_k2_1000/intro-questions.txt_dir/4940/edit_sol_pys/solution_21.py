

# This is the solution to the "File" problem on Kattis
# https://open.kattis.com/problems/file

N, M = [int(x) for x in input().split()] # N is the number of people, M is the number of stages

times = [] # times is a list of lists, where each list is a person's times for each stage
for i in range(N):
    times.append([int(x) for x in input().split()])

#print(times) # for testing

# sort the times by the first stage, then the second stage, then the third stage
times.sort(key = lambda x: x[0])
times.sort(key = lambda x: x[1])
times.sort(key = lambda x: x[2])

#print(times) # for testing

# now we can just add up the times for each person
total_times = []
for i in range(N):
    total_time = 0
    for j in range(M):
        total_time += times[i][j]
    total_times.append(total_time)

# print the total times
for i in range(N):
    print(total_times[i], end=" ")
print()
