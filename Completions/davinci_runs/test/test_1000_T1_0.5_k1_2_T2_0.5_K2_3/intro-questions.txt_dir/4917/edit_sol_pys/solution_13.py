

num_times = int(input())

times = []
for i in range(num_times):
    times.append([int(x) for x in input().split()]) # list comprehension

# Check if all times are the same
for i in range(num_times - 1):
    if times[i][1] != times[i + 1][1]:
        print("Edward is right")
        exit()

print("Gunilla has a point")
