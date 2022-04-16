

n = int(input())  # Number of elements in the list
t = list(map(int, input().split()))  # List of temperatures

# Sort the temperatures
t.sort()

# Initialize the minimum temperature difference
min_temp_diff = 100

# Initialize the list of sorted temperatures
sorted_t = []

for i in range(n):
    for j in range(n):
        if t[j] - t[i] < min_temp_diff:
            min_temp_diff = t[j] - t[i]
            sorted_t = [t[i], t[j]]

print(sorted_t)
