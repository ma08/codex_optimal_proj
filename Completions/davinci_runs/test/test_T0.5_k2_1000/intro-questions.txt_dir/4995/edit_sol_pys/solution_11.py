

# Number of observations
N = int(input())

# List of tuples (minutes, seconds)
data = []

# Get data from user
for i in range(N):
    data.append(tuple(int(x) for x in input().split()))

def average(data):
    total = 0
    for i in data:
        total += i[1]
    return total/N

# If average length is shorter than or equal to a normal minute, print "measurement error"
if total/N <= 60:
    print("measurement error")
else:
    print(total/N/60)
