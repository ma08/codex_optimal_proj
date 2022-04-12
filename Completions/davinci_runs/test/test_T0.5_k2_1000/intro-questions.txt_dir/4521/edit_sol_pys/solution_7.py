

n = int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))

# Sort by coordinate (x)
x_sorted = sorted(zip(x, v), key=lambda x: x[0])
# Sort by speed (v)
v_sorted = sorted(zip(x, v), key=lambda x: x[1])

# Get coordinates of first point (x)
first_x = x_sorted[0][0]
# Get coordinates of last point (x)
last_x = x_sorted[-1][0]

# Get speeds of first point (v)
first_v = x_sorted[0][1]
# Get speeds of last point (v)
last_v = x_sorted[-1][1]

# Get time when first point will overtake last point
t = (last_x - first_x) / (first_v - last_v)

# Get coordinates of first point at time t (x)
first_t = first_x + t * first_v
# Get coordinates of last point at time t (x)
last_t = last_x + t * last_v

# Sum of minimum distances over all pairs of points (s)
s = 0

# If first point overtakes last point, then minimum distance between 1st and 2nd point is 0
if first_t < last_t:
	s += 0
# Otherwise, minimum distance between 1st and 2nd point is distance between 1st and 2nd point at time t
else:
	s += (x_sorted[1][0] - x_sorted[0][0]) - (x_sorted[1][1] - x_sorted[0][1]) * t

# If last point overtakes first point, then minimum distance between n-1th and nth point is 0
if last_t < first_t:
	s += 0
# Otherwise, minimum distance between n-1th and nth point is distance between n-1th and nth point at time t
else:
	s += (x_sorted[-1][0] - x_sorted[-2][0]) - (x_sorted[-1][1] - x_sorted[-2][1]) * t

# Get number of points between 1st and 2nd point (n1)
n1 = -1
for i in range(1, n):
	if x_sorted[i][0] < first_t:
		n1 += 1
	else:
		break

# Get number of points between n-1th and nth point (n2)
n2 = -1
for i in range(1, n):
	if x_sorted[-i][0] > last_t:
		n2 += 1
	else:
		break

# Get number of points between 2nd and n-1th point (n3)
n3 = n - n1 - n2 - 2

# Add distances between points in the first group
for i in range(n1):
	s += (x_sorted[i+1][0] - x_sorted[i][0]) - (x_sorted[i+1][1] - x_sorted[i][1]) * t

# Add distances between points in the second group
for i in range(n2):
	s += (x_sorted[-i-1][0] - x_sorted[-i-2][0]) - (x_sorted[-i-1][1] - x_sorted[-i-2][1]) * t

# Add distances between points in the third group
for i in range(n3):
	s += (x_sorted[n1+i+2][0] - x_sorted[n1+i+1][0]) - (x_sorted[n1+i+2][1] - x_sorted[n1+i+1][1]) * t

# Add distances between points in the first and second group
for i in range(n1):
	for j in range(n2):
		s += abs(x_sorted[i+1][0] - x_sorted[-j-1][0]) - abs(x_sorted[i+1][1] - x_sorted[-j-1][1]) * t

# Add distances between points in the first and third group
for i in range(n1):
	for j in range(n3):
		s += abs(x_sorted[i+1][0] - x_sorted[n1+j+2][0]) - abs(x_sorted[i+1][1] - x_sorted[n1+j+2][1]) * t

# Add distances between points in the second and third group
for i in range(n2):
	for j in range(n3):
		s += abs(x_sorted[-i-1][0] - x_sorted[n1+j+2][0]) - abs(x_sorted[-i-1][1] - x_sorted[n1+j+2][1]) * t

# Print sum (s)
print(int(s))
