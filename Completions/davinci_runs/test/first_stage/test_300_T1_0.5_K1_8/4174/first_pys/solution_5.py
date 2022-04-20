

# get inputs
n, x = map(int, input().split())
l = list(map(int, input().split()))

# create list of coordinates
coordinates = [0]
for i in range(n):
    coordinates.append(coordinates[i] + l[i])

# count the number of bounces where the coordinate is at most x
count = 0
for coordinate in coordinates:
    if coordinate <= x:
        count += 1

print(count)