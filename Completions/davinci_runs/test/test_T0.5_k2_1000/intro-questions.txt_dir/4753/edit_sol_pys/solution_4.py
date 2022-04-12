
# SOLUTION

# Accept the number of vertices
n = int(input())

# Initialize the number of diagonals
d = 2 * n - 5

# Initialize the number of intersections
i = n - 3

# Initialize the count of diagonals that intersect
d_i = 0

# For each diagonal
for _ in range(d):
    # Add the number of intersections for this diagonal
    d_i += i
    # Decrement the number of intersections
    i -= 1

# Print the number of intersections
print(d_i)
