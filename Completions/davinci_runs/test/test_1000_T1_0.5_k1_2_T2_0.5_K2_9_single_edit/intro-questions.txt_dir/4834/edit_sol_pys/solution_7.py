
N = int(input())
times = list(map(int, input().split()))

# Sort the times in descending order
times.sort(reverse=True)

# Greedy algorithm
# The one with the shortest time should go first
# the second shortest time should go second, etc.
# and the longest time should go last

# The time it takes to finish all lectures is the sum of the times
print(sum(times))
