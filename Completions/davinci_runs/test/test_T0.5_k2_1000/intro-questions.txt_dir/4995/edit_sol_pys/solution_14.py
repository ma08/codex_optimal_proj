

# Number of observations.
N = int(input())

# List of tuples (minutes, seconds).
data = []

# Get data from user.
for i in range(N):
    data.append(tuple(int(x) for x in input().split()))

# Calculate average length of an SL minute.
total = 0
for i in data:
    total += i[1]

# If average length is shorter than or equal to a normal minute, print "measurement error".
if total/N <= 60:
    print("measurement error")
else:
    print(total/N/60)
