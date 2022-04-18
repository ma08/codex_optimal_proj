n = int(input())
a = [int(i) for i in input().split()]


# Find the first 0 in a
i = 0
while i < n and a[i] == 1:
    i += 1

# Add the rest of the 1s
max_length = sum(a[:i])

# Find the maximal length of 1s in a
length = 0
for j in range(i, n - 1):
    if a[j] == 0:
        max_length = max(max_length, length)
        length = 0
    else:
        length += 1
    else:
        max_length = max(max_length, length)
        length = 0
max_length = max(max_length, length)

# Add the rest of the 1s
max_length += sum(a[:i])

print(max_length)
