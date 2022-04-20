

# Read input
A, B, C, D = [int(x) for x in input().split()]

# Count the number of integers that are not divisible by C or D
count = 0
for i in range(A, B+1):
    if i % C != 0 and i % D != 0:
        count += 1

# Print the result
print(count)