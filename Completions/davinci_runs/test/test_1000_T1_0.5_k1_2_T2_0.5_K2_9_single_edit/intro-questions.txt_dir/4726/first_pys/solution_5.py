

# Get input
m, n, t = map(int, input().split())

# Calculate the time complexity
if t == 1:
    time_complexity = n
elif t == 2:
    time_complexity = 2**n
elif t == 3:
    time_complexity = n**4
elif t == 4:
    time_complexity = n**3
elif t == 5:
    time_complexity = n**2
elif t == 6:
    time_complexity = n*(math.log(n, 2))
elif t == 7:
    time_complexity = n

# Check if the time complexity is less than or equal to m
if time_complexity <= m:
    print("AC")
else:
    print("TLE")