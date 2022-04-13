

# SOLUTION

# Read the number of vertices
n = int(input("Enter the number of vertices: "))

# Initialize the number of diagonals and intersections
d = 2 * n - 5  # number of diagonals
i = n - 3  # number of intersections

d_i = 0  # number of diagonals that intersects

# For each diagonal
for _ in range(d):
    # Add the number of intersections for this diagonal
    d_i += i
    # Decrement the number of intersections
    i -= 1

# Print the number of intersections
print(d_i)
