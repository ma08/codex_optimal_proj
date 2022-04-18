
# Solution

# Get input
r, n = [int(x) for x in input().split()]

# Create list of rooms and fill with 0's
rooms = [0] * (r + 1)

# Get taken rooms
for i in range(n):
    rooms[int(input())] = 1

# Check if there is a room available
    if rooms[i] == 0:
        print(i)
        break
else:
    print('too late')


# Solution
# Get input
r, n = [int(x) for x in input().split()]

# Create list of rooms and fill with 0's
rooms = [0] * (r + 1)

# Get taken rooms
for i in range(n):
    rooms[int(input())] = 1

# Check if there is a room available
for i in range(1, r + 1):
    if rooms[i] == 0:
        print(i + 1)
        break
else:
    print('too late')
