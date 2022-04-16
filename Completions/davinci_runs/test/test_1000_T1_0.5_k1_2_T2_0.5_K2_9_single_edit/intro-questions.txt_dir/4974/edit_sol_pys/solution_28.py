
import sys
# Solution

# Get input
r, n = [int(x) for x in input().split()]

# Create a list of rooms and fill with 0's
rooms = [0] * r

# Get taken rooms
for i in range(n):
    rooms[int(input()) - 1] = 1

# Check if there is a room available
for i in range(r):
    if rooms[i] == 0:
        sys.stdout.write(str(i + 1))
        break
else:
    sys.stdout.write("too late")
