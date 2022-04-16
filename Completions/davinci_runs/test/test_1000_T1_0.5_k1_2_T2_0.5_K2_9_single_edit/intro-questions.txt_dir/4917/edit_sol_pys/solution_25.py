
num_times = int(input())

times = []
for i in range(num_times):
    times.append([int(x) for x in input().split()])

# Check if all times are the same
for i in range(num_times - 1):
    if times[i][1] != times[i + 1][1]:
        print("edward is right")
        exit()

print("gunilla has a point")
