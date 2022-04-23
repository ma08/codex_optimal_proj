

n = int(input())
a = list(map(int, input().split()))

# Find the maximum length of 1s
max_length = 0
length = 0
for i in range(n):
    if a[i] == 1:
        length += 1
    else:
        max_length = max(max_length, length)
        length = 0
max_length = max(max_length, length)

# Print the result
print(max_length)
