

n = int(input())
a = list(map(int, input().split()))

# Find the first 0 and count the 1s before it
count = 0
i = 0
while a[i] == 1:
    count += 1
    i += 1

# Find the maximal length of 1s between 0s
max_length = 0
length = 0
for j in range(i, n):
    if a[j] == 1:
        length += 1
    else:
        max_length = max(max_length, length)
        length = 0
max_length = max(max_length, length)

# Add the 1s before the first 0
max_length += count

print(max_length)
