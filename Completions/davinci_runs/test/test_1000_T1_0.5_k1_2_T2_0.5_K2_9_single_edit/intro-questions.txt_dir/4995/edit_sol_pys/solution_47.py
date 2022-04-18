

# Calculate average length of an S.L. minute
def calculate_average(data):
    total = 0
    for i in data:
        total += i[1]
    return total/len(data)/60

# If average length is shorter than or equal to a normal minute, print "measurement error"
def print_result(average):
    if average <= 60:
        print("measurement error")
    else:
        print(average)

# Main

# Number of observations
N = int(input())

# List of tuples (minutes, seconds)
data = []

# Get data from user
for i in range(N):
    data.append(tuple(int(x) for x in input().split()))
print_result(calculate_average(data))
