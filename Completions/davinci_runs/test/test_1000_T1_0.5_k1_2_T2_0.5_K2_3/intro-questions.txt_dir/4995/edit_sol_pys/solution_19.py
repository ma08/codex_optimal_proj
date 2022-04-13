

# Number of test cases
T = int(input())

for i in range(T):
    # Number of observations
    N = int(input())

    # List of tuples (minutes, seconds)
    data = []

    # Get data from user
    for j in range(N):
        data.append(tuple(int(x) for x in input().split()))

    # Calculate average length of a S.L. minute
    total = 0
    for j in data:
        total += j[1]

    # If average length is shorter than or equal to a normal minute, print "measurement error"
    if total/N <= 60:
        print("measurement error")
    else:
        print(total/N/60)
