

# Read input
a = int(input())

# Initialize
result = 0

# Calculate
for i in range(a):
    for j in range(a):
        for k in range(a):
            result += 1

# Print result
print(result)