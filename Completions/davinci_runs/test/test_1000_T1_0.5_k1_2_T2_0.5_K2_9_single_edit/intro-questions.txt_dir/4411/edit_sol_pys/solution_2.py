
#-----Solution-----

# First, we find the number of segments that cover each point.
# Then, we iterate through the list of points, and for each point, we check how many segments cover it.
# If the number of segments covering the point is greater than k, we add the point to the list of positions to remove.
# We also add the segments that cover the point to the list of segments to remove.
# We then remove the segments from the list of segments.
# We repeat the process until we find no more positions to remove.

# The number of segments that cover each point
segments_covering_point = [0] * (2 * (10**5) + 1)

# The positions of the points to remove
positions_to_remove = []

# The segments to remove
segments_to_remove = []

# Read in the number of segments and the maximum number of segments per point
n, k = [int(x) for x in input().split()]

# Read in all of the segments
segments = []
for i in range(n):
    segments.append([int(x) for x in input().split()])

# Iterate through all of the segments
for i in range(n):
    # Iterate through all of the points covered by the segment
    for j in range(segments[i][0], segments[i][1] + 1):
        # Increment the number of segments covering the point
        segments_covering_point[j] += 1

# Iterate through all of the points
for i in range(2 * (10**5) + 1):
    # If the number of segments covering the point is greater than k
    if segments_covering_point[i] > k:
        # Add the point to the list of positions to remove
        positions_to_remove.append(i)

# Iterate through all of the positions to remove
for position in positions_to_remove:
    # Iterate through all of the segments
    for i in range(n):
        # If the segment covers the position to remove
        if segments[i][0] <= position and position <= segments[i][1]:
            # Add the segment to the list of segments to remove
            segments_to_remove.append(i + 1)
            # Break out of the loop
            break

# Iterate through all of the segments to remove
for segment in segments_to_remove:
    # Remove the segment from the list of segments
    segments.remove(segments[segment - 1])

# Print the number of segments to remove
print(len(segments_to_remove))

# Print the segments to remove
for i in range(len(segments_to_remove)):
    print(segments_to_remove[i], end = " ")
