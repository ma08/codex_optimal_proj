
n = int(input())
s = input()

# first half and second half
first_half = s[:n // 2]
second_half = s[n // 2:]

# calculate operations
operations_1 = abs(first_half.count('a') - first_half.count('b'))
operations_2 = abs(second_half.count('a') - second_half.count('b'))

# find the minimum operations
operations = min(operations_1, operations_2)

print(operations)

# modified string
if operations_1 < operations_2:
    print(first_half + second_half)
else:
    print(second_half + first_half)
