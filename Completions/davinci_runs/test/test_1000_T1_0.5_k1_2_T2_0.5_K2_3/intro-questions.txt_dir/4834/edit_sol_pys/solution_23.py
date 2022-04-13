

N = int(input())
times = list(map(int, input().split()))

# Sort the times in ascending order
times.sort()

# Greedy algorithm
# The one with the longest time should go first
# The second longest time should go second, etc.
# The shortest time should go last (this is the only time it will be waiting, so it doesn't matter)

# The time it takes to finish all lectures is the sum of the times
print(sum(times[i] * (N - i) for i in range(N)))
