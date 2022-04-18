

# Get input
n = int(input())
a = list(map(int, input().split()))

# Sort the list
a.sort()

# Print the index of the unique max element
print(a.index(a[-1]) + 1)
