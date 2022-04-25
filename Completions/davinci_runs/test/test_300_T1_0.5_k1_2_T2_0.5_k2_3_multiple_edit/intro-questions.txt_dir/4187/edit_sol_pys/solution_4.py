
n = int(input())
numbers = list(map(int, input().split()))
# Find the first zero
i = 0
while numbers[i] == 1:
    i += 1
# Find the maximal length of ones
max_length = 0
length = 0
for j in range(i, n):
    if numbers[j] == 1:
        length += 1
    else:
        max_length = max(max_length, length)
        length = 0
max_length = max(max_length, length)
# Add the rest of the ones
max_length += sum(numbers[:i])
print(max_length)
