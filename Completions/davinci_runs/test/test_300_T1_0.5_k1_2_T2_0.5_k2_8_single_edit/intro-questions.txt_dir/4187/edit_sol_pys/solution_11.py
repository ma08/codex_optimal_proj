

n = int(input())
a = list(map(int, input().split()))

# Find the first 0
i = 0
while a[i] == 1:
    i += 1

# Find the maximal length of 1s in the beginning
length_begin = 0
for j in range(i):
    if a[j] == 1: length_begin += 1

# Find the maximal length of 1s in the end
length_end = 0
for j in range(n - 1, i, -1):
    if a[j] == 1: length_end += 1

# Find the maximal length of 1s in the middle
max_length_middle = 0
length_middle = 0
for j in range(i, n - 1):
    if a[j] == 1: length_middle += 1
    elif a[j] == 0 and a[j + 1] == 1: length_middle = 0
    else:

# Add the rest of the 1s
max_length += sum(a[:i])

print(max_length)
