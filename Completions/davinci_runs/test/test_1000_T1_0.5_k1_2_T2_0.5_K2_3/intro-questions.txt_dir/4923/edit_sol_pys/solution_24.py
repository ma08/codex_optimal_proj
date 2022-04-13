
# Get input
n = int(input())
a = list(map(int, input().split()))

# Sort the list
a.sort()

# Find the index of the unique max element
for i in range(len(a)):
    if a[i] == a[-1]:
        print(i + 1)
        break
