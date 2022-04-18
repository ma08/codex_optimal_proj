
# Solution

# Number of teams
N = int(input())
# Time required for the i-th team to understand and implement an algorithm
T = list(map(int, input().split()))

# Sorted times.
# This is a stable sort.
T.sort(reverse=True)

total_time = 0

# When the number of teams is even.
if N % 2 == 0:
    for i in range(0, N, 2):
        total_time += T[i]
    for i in range(1, N, 2):
        total_time += T[i]

# When the number of teams is odd.
else:
    for i in range(1, N, 2):
        total_time += T[i]
    for i in range(0, N, 2):
        total_time += T[i]

print(total_time)
