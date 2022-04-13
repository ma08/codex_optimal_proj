

# Get input from user
n = int(input())
a = list(map(int, input().split()))

# Sort the list in ascending order
a.sort()

# Find the index of the unique max element
for i in range(len(a)):
    if a[i] == a[-1]:
        print(i + 1)
        break
