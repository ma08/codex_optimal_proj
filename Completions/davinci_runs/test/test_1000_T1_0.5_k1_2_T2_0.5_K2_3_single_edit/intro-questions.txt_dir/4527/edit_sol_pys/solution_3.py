
# Greedy Algorithm

t = int(input())  # number of test cases

for _ in range(t):  # iterate over the test cases
    n = int(input())  # number of activities
    activities = []  # list of activities
    for __ in range(n):  # iterate over the activities
        activities.append(list(map(int, input().split())))
    activities.sort(key=lambda x: x[1])  # sort by finish time
    count = 0
    j = 0
    for i in range(n):
        if activities[i][0] >= activities[j][1]:
            count += 1
            j = i
    print(count)
