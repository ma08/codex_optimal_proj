

# Solution 1

# Get input
r, n = [int(x) for x in input().split()]

# Get taken rooms
taken = []
for i in range(n):
    taken.append(int(input()))

# Check if there is a room available
for i in range(1, r + 1):
    if i not in taken:
        print(i)
        break
else:
    print("too late")


# Solution 2

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
        print(i + 1)
        break
else:
    print("too late")
