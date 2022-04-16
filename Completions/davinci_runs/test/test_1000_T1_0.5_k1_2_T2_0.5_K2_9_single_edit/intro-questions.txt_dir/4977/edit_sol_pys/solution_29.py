
a, b = [int(x) for x in input().split()]  # initial coordinates
c, d = [int(x) for x in input().split()]  # final coordinates
t = int(input())

# If the start and end points are the same, then we can do a U-turn and get there.
if a == c and b == d:
    print("Y")
    exit()

# If we are trying to travel more than t units, we can't get there.
if abs(a-c) + abs(b-d) > t:
    print("N")
    exit()

# If we are trying to travel less than t units, we can't get there.
if abs(a-c) + abs(b-d) < t:
    print("N")
    exit()

# If we are trying to travel exactly t units, we can get there.
if abs(a-c) + abs(b-d) == t:
    print("Y")
    exit()
