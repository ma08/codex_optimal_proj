

num_times = int(input())  # Number of times Edward and Gunilla meet

times = []
for i in range(num_times):  # Read all times
    times.append([int(x) for x in input().split()])  # Split input into a list of integers

# Check if all times are the same
for i in range(num_times - 1):
    if times[i][1] != times[i + 1][1]:
        print("edward is right")
        exit()

print("gunilla has a point")
