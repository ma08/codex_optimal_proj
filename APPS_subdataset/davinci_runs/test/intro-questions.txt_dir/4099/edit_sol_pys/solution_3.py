

# Read input
n = int(input())
a = [int(x) for x in input().split()] + [0]

# Initialize the answer
ans = 0

# Loop through the elements of the array
for i in range(n):
    # If the current element is 0, add 1 to the answer
    if a[i] == 0:
        ans += 1
    # Otherwise, add 1 to the current element
    else:
        a[i] += 1

# Print the answer
print(ans)
