

n = int(input())
a = list(map(int, input().split()))

# Find the first 0.
i = 0
while a[i] == 1:
    i += 1

# Find the maximal length of 1s.
max_length = 0
length = 0
for j in range(i, n):
    if a[j] == 1:
        length += 1
    else:
        max_length = max(max_length, length)
        length = 0
max_length = max(max_length, length)

# Add the rest of the 1s.
max_length += sum(a[:i])

print(max_length)
