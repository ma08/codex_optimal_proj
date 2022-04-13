

N = int(input()) # Number of observations

data = [] # List of tuples (minutes, seconds)

# Get data from user
for i in range(N):
    data.append(tuple(int(x) for x in input().split()))

# Calculate average length of a S.L. minute
total = 0
for i in data:
    total += i[1]

# If average length is shorter than or equal to a normal minute, print "measurement error" and end
if total/N <= 60:
    print("measurement error")
else:
    print(int(total/N/60))
