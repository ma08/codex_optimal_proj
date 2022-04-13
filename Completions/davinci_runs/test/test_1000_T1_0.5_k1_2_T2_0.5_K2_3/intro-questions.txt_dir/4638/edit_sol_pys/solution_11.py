

# SOLUTION
n, c = [int(x) for x in input().split()] # n = number of floors, c = speed of elevator
a = [int(x) for x in input().split()] # a = speed of stairs
b = [int(x) for x in input().split()] # b = time to open the elevator

# Using the elevator
elevator = [c + b[0]]
for i in range(1, n - 1):
    elevator.append(elevator[i - 1] + c + b[i])

# Using the stairs
stairs = [0]
for i in range(1, n - 1):
    stairs.append(stairs[i - 1] + a[i - 1])

# Compute minimum
t = [0]
for i in range(1, n):
    t.append(min(elevator[i - 1], stairs[i - 1]))

print(*t)
