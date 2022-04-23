n = int(input())
a = list(map(int, input().split()))

# Find the first person who has a gift
i = 1
while a[i - 1] != 0:
    i = i + 1

# Assign gifts to people who don't have one
j = i + 1
while j <= n + 1:
    if a[j - 1] == 0:
        a[j - 1] = i
        i = i + 1
    j = j + 1

# Print out the people
print(*a)
