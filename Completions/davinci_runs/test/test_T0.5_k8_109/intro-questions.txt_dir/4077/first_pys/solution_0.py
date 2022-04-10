

#-----Solution-----

n, m = map(int, input().split())
a = list(map(int, input().split()))

# Create initial empty lists
left = []
right = []

# Create a list of all possible sums of two numbers in the given array
for i in range(n):
    for j in range(i+1, n+1):
        left.append(a[i])
        right.append(a[j-1])

# Create a new list with all possible sums of two numbers in the given array
sums = [sum(x) for x in zip(left, right)]

# Create a list of all possible medians in the given array
medians = []
for i in range(len(sums)):
    if i % 2: # if the number of elements in the list is odd, the median is the middle element
        medians.append(sums[i] // 2)
    else: # if the number of elements in the list is even, the median is the average of the two middle elements
        medians.append((sums[i] + sums[i+1]) // 2)

# Print the number of times the given median occurs in the medians list
print(medians.count(m))