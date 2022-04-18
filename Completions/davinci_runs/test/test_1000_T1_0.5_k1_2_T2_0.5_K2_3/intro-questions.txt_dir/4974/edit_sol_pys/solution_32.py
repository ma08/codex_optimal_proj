

# Solution

# Get input
r, n = [int(x) for x in raw_input().split()]

# Create a list of rooms and fill with 0's
rooms = [0] * r

# Get taken rooms
for i in range(n):
    rooms[int(raw_input()) - 1] = 1

# Check if there is a room available
for i in range(r):
    if rooms[i] == 0:
        print(i + 1)
        break
else:
    print("too late")
