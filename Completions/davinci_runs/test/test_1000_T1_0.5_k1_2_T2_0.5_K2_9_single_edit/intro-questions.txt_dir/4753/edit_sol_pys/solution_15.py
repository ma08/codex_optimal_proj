

# SOLUTION

# Accept the number of vertices
n = int(input())

# Initialize the count of diagonals that intersect
d_i = 0

# For each diagonal, starting with the 3rd
for i in range(n - 3, 0, -1):
    # Add the number of intersections for this diagonal
    d_i += i

# Print the number of intersections
print(d_i)
