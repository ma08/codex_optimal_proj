

# SOLUTION

# Accept the number of vertices
n = int(input())

# Initialize the number of diagonals and intersection
d = 2 * n - 5  # diagonals
i = n - 3  # intersections

# Initialize the count of diagonals that intersects
d_i = 0

# For each diagonal
for _ in range(d):
    # Add the number of intersections for this diagonal
    d_i += i
    # Decrement the number of intersections
    i -= 1
 
# Print the number of intersections
print(d_i)
