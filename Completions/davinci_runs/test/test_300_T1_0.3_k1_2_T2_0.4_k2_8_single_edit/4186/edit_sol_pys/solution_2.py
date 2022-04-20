

n, k = map(int, input().split())
a = list(map(int, input().split()))[:n]

# Create a dictionary of numbers and their counts
numbers = {}
for num in a:
    if num not in numbers:
        numbers[num] = 1
    else:
        numbers[num] += 1

# Find the number of numbers that can be formed
num_numbers = 0
for i in numbers:
    num_numbers += numbers[i] // 2

# Find the number of numbers that need to be solved
num_numbers = 0
for i in numbers:
    num_numbers += numbers[i] % 2

# Print the answer
print(num_numbers + (n // 2) - num_numbers)
