
N = int(input())
times = list(map(int, input().split()))

# Greedy algorithm
# The one with the shortest time should go first
# The second shortest time should go second, etc.
# and the longest time should go last (this is the only time it will be waiting, so it doesn't matter)
# Sort the times in descending order
times.sort(reverse=True)


# The time it takes to finish all lectures is the sum of the times
print(sum(times))
