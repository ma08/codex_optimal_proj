

n = int(input())
a = list(map(int, input().split()))

# Find the first 0
i = 0
while a[i] == 1:
    i += 1

# Find the maximum length of 1s
max_len = 0
length = 0
for j in range(i, n):
    if a[j] == 1:
        length += 1
    else:
        max_len = max(max_len, length)
        length = 0
max_len = max(max_len, length)

# Add the rest of the 1s
max_len += sum(a[:i])

print(max_len)
