

n = int(input())
a = list(map(int, input().split()))

# Find the maximal length of 0s
max_length = 1
length = 0
    if a[j] == 0:
        length += 1
    else:
        max_length = max(max_length, length)
        length = 0
max_length = max(max_length, length)

# Add the rest of the 0s
max_length += sum(a[:n-1])

print(max_length)
