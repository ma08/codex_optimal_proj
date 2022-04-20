

import sys

# Read in the input
raw_input = sys.stdin.read()
tokens = raw_input.split()

n = int(tokens[0])
m = int(tokens[1])

a = list(map(int, tokens[2:2+n]))

l = [None] * m
r = [None] * m

for i in range(m):
    l[i] = int(tokens[2+n+2*i])
    r[i] = int(tokens[2+n+2*i+1])

# This is the maximum possible value for the difference
# of the min and max elements in the array.
d = 0

# This is the number of segments to apply.
q = 0

# This is the list of segments to apply.
c = []

# This is the index of the segment that is currently
# being considered.
i = 0

# This is the index of the element in the array that
# is currently being considered.
j = 0

# This is the current minimum element in the array.
min = a[0]

# This is the current maximum element in the array.
max = a[0]

# Find the maximum value for the difference of the min
# and max elements in the array.
while i < m:
    # If the current element is in the current segment,
    # then update the min and max values.
    if j >= l[i] and j <= r[i]:
        if a[j] < min:
            min = a[j]
        if a[j] > max:
            max = a[j]
    # If the current element is not in the current segment,
    # then check if adding the current segment would increase
    # the maximum difference of the min and max elements.
    else:
        # If the current segment is within the current min and max
        # values, then adding the current segment would not increase
        # the maximum difference of the min and max elements.
        if min <= a[l[i]-1] and a[r[i]-1] <= max:
            pass
        # Otherwise, adding the current segment would increase the
        # maximum difference of the min and max elements.
        else:
            # If the current difference of the min and max elements
            # is less than the maximum difference of the min and max
            # elements, then update the maximum difference and the
            # list of segments to apply.
            if max - min < max - a[l[i]-1] + a[r[i]-1] - min:
                d = max - a[l[i]-1] + a[r[i]-1] - min
                q = 1
                c = [i+1]
            # If the current difference of the min and max elements
            # is equal to the maximum difference of the min and max
            # elements, then add the current segment to the list of
            # segments to apply.
            elif max - min == max - a[l[i]-1] + a[r[i]-1] - min:
                q += 1
                c.append(i+1)
        # Move on to the next segment.
        i += 1
    # Move on to the next element in the array.
    j += 1

# Print out the results.
print(d)
print(q)
for i in range(q):
    print(c[i], end='')
    if i < q-1:
        print(' ', end='')
print()