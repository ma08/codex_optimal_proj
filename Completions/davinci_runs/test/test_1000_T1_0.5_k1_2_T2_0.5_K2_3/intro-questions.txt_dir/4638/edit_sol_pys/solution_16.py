
# SOLUTION
n, c = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Using elevator.
elevator = [c + b[0]]
for i in range(1, n - 1):
    elevator.append(elevator[i - 1] + c + b[i])

# Using stairs.
stairs = [0]
for i in range(1, n - 1):
    stairs.append(stairs[i - 1] + a[i - 1])

# Compute minimum.
t = [0]
for i in range(1, n):
    t.append(min(elevator[i - 1], stairs[i - 1]))

print(*t)
