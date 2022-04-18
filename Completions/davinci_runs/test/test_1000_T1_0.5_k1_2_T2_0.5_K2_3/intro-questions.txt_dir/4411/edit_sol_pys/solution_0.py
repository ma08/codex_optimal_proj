

#-----Solution 2-----

# We iterate through all of the segments.
# For each segment, we add it to the list of segments to remove.
# Then, we iterate through all of the segments following the current segment.
# If the current segment and the following segment overlap, we remove the following segment from the list of segments to remove.
# We repeat this process until no more segments overlap.

# The number of segments to remove
segments_to_remove_count = 0

# The segments to remove
segments_to_remove = []

# Read in the number of segments and the maximum number of segments per point
n, k = [int(x) for x in input().split()]

# Read in all of the segments
segments = []
for i in range(n):
    segments.append([int(x) for x in input().split()])

# Iterate through all of the segments, except for the last segment
for i in range(n - 1):
    # Add the segment to the list of segments to remove
    segments_to_remove.append(i + 1)

    # Iterate through all of the segments following the current segment, except for the last segment
    for j in range(i + 1, n - 1):
        # If the current segment and the following segment overlap
        if segments[i][1] > segments[j][0]:
            # Remove the following segment from the list of segments to remove
            segments_to_remove.remove(j + 1)

# Add the last segment to the list of segments to remove
segments_to_remove.append(n)

# Print the number of segments to remove, followed by a space
print(len(segments_to_remove), end=" ")

# Print the segments to remove
for segment in segments_to_remove:
    print(segment, end=" ")
